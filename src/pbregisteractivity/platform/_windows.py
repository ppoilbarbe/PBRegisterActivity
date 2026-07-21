"""Windows platform services.

The data directory (``%APPDATA%``) and the single-instance lock (``msvcrt``)
are Windows-specific and get their own implementation here. Only the
executable resolution helper and the exception type are reused as-is from
``_linux.py``, plus the ``Installer.apply()`` dispatch method inherited
through subclassing.
"""

import os
import subprocess
import sys
from pathlib import Path

from ._linux import _APP_ID, _APP_NAME, SingleInstanceException, executable_path
from ._linux import Installer as _LinuxInstaller

__all__ = ["SingleInstance", "SingleInstanceException", "app_dir", "installer"]


def app_dir() -> Path:
    """Return the application's data directory (``%APPDATA%\\pbregisteractivity\\``),
    creating it if needed."""
    base = os.environ.get("APPDATA")
    p = Path(base) / _APP_ID if base else Path.home() / "AppData" / "Roaming" / _APP_ID
    p.mkdir(parents=True, exist_ok=True)
    return p


class SingleInstance:
    """Byte-range lock (msvcrt.locking) on a lock file."""

    def __init__(self, lock_file: str) -> None:
        import msvcrt

        self._initialized = False
        self._lock_file = lock_file
        self._fp = open(lock_file, "w")  # noqa: SIM115
        self._fp.flush()
        try:
            msvcrt.locking(self._fp.fileno(), msvcrt.LK_NBLCK, 1)
        except OSError:
            print(
                "Application déjà en cours de fonctionnement, fermeture.",
                file=sys.stderr,
            )
            raise SingleInstanceException()
        self._initialized = True

    def __del__(self) -> None:
        if not self._initialized:
            return
        import msvcrt

        try:
            self._fp.seek(0)
            msvcrt.locking(self._fp.fileno(), msvcrt.LK_UNLCK, 1)
        except OSError:
            pass
        self._fp.close()
        try:
            os.unlink(self._lock_file)
        except OSError:
            pass


# ---------------------------------------------------------------------------
# System registration
# ---------------------------------------------------------------------------

_REG_KEY = r"Software\Microsoft\Windows\CurrentVersion\Run"


def _start_menu_shortcut() -> Path:
    appdata = os.environ.get("APPDATA")
    base = Path(appdata) if appdata else Path.home() / "AppData" / "Roaming"
    return (
        base / "Microsoft" / "Windows" / "Start Menu" / "Programs" / f"{_APP_NAME}.lnk"
    )


def _powershell_quote(value: str) -> str:
    return value.replace("'", "''")


class Installer(_LinuxInstaller):
    def install_app(self) -> None:
        dest = _start_menu_shortcut()
        dest.parent.mkdir(parents=True, exist_ok=True)
        exe = executable_path()
        script = (
            "$s = (New-Object -ComObject WScript.Shell)."
            f"CreateShortcut('{_powershell_quote(str(dest))}'); "
            f"$s.TargetPath = '{_powershell_quote(exe)}'; "
            f"$s.WorkingDirectory = '{_powershell_quote(str(Path(exe).parent))}'; "
            "$s.Save()"
        )
        subprocess.run(
            ["powershell", "-NoProfile", "-NonInteractive", "-Command", script],
            check=True,
        )

    def uninstall_app(self) -> None:
        _start_menu_shortcut().unlink(missing_ok=True)

    def install_autostart(self) -> None:
        import winreg

        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, _REG_KEY)
        try:
            winreg.SetValueEx(key, _APP_NAME, 0, winreg.REG_SZ, executable_path())
        finally:
            winreg.CloseKey(key)

    def uninstall_autostart(self) -> None:
        import winreg

        try:
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER, _REG_KEY, 0, winreg.KEY_SET_VALUE
            )
        except FileNotFoundError:
            return
        try:
            winreg.DeleteValue(key, _APP_NAME)
        except FileNotFoundError:
            pass
        finally:
            winreg.CloseKey(key)


installer = Installer()
