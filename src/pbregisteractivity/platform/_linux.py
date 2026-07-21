"""Linux platform services: data directory, single-instance lock and
system registration (application menu entry, autostart).

Linux is the reference POSIX implementation: macOS (``_macos.py``) reuses
whatever behaves identically here (data directory, single-instance lock,
executable resolution) and only overrides what actually differs (system
registration). Windows (``_windows.py``) only reuses the executable
resolution helper and the exception type, and the ``Installer.apply()``
dispatch method inherited through subclassing.
"""

import fcntl
import os
import shutil
import struct
import sys
from pathlib import Path

_APP_NAME = "PBRegisterActivity"
_APP_ID = _APP_NAME.lower()
_APP_COMMENT = "Enregistrement d'activités pour remplissage de CRA"

_PACKAGE_DIR = Path(__file__).resolve().parent.parent
_ICON_SOURCE = _PACKAGE_DIR / "resources" / f"{_APP_ID}.png"


def app_dir() -> Path:
    """Return the application's data directory (``~/.pbregisteractivity/``),
    creating it if needed."""
    p = Path.home() / f".{_APP_ID}"
    p.mkdir(parents=True, exist_ok=True)
    return p


def executable_path() -> str:
    """Resolve the path/command used to relaunch the application."""
    if getattr(sys, "frozen", False):
        return sys.executable
    return shutil.which(_APP_ID) or sys.executable


class SingleInstanceException(BaseException):
    """Raised when another instance of the program is already running."""


class SingleInstance:
    """POSIX advisory file lock (fcntl.lockf), used by Linux and macOS."""

    def __init__(self, lock_file: str) -> None:
        self._initialized = False
        self._lock_file = lock_file
        self._fp = open(lock_file, "w")  # noqa: SIM115
        self._fp.flush()
        try:
            fcntl.lockf(self._fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            print(
                "Application déjà en cours de fonctionnement ailleurs et "
                "pas forcément sur ce poste, fermeture.",
                file=sys.stderr,
            )
            raise SingleInstanceException()
        self._initialized = True

    def __del__(self) -> None:
        if not self._initialized:
            return
        fcntl.lockf(self._fp, fcntl.LOCK_UN)
        if os.path.isfile(self._lock_file):
            os.unlink(self._lock_file)


# ---------------------------------------------------------------------------
# System registration
# ---------------------------------------------------------------------------


def _xdg_data_home() -> Path:
    value = os.environ.get("XDG_DATA_HOME")
    return Path(value) if value else Path.home() / ".local" / "share"


def _xdg_config_home() -> Path:
    value = os.environ.get("XDG_CONFIG_HOME")
    return Path(value) if value else Path.home() / ".config"


def _desktop_file(*, autostart: bool) -> Path:
    base = (
        _xdg_config_home() / "autostart"
        if autostart
        else _xdg_data_home() / "applications"
    )
    return base / f"{_APP_ID}.desktop"


def _desktop_content(*, autostart: bool) -> str:
    lines = [
        "[Desktop Entry]",
        "Type=Application",
        f"Name={_APP_NAME}",
        f"Comment={_APP_COMMENT}",
        f"Exec={executable_path()}",
        f"Icon={_APP_ID}",
        "Terminal=false",
        "Categories=Office;",
    ]
    if autostart:
        lines.append("X-GNOME-Autostart-enabled=true")
    return "\n".join(lines) + "\n"


def _png_size(path: Path) -> tuple[int, int]:
    # Minimal PNG parsing: width/height are the first 8 bytes of the IHDR
    # chunk, which always immediately follows the 8-byte PNG signature.
    data = path.read_bytes()[16:24]
    return struct.unpack(">II", data)


def _icon_dest() -> Path:
    width, height = _png_size(_ICON_SOURCE)
    return (
        _xdg_data_home()
        / "icons"
        / "hicolor"
        / f"{width}x{height}"
        / "apps"
        / f"{_APP_ID}.png"
    )


class Installer:
    """System registration (application menu entry + autostart).

    ``apply()`` is shared by every platform; subclasses in ``_macos.py`` and
    ``_windows.py`` only override the four primitives below.
    """

    def install_app(self) -> None:
        dest = _icon_dest()
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(_ICON_SOURCE, dest)

        desktop = _desktop_file(autostart=False)
        desktop.parent.mkdir(parents=True, exist_ok=True)
        desktop.write_text(_desktop_content(autostart=False), encoding="utf-8")

    def uninstall_app(self) -> None:
        _desktop_file(autostart=False).unlink(missing_ok=True)
        icons_root = _xdg_data_home() / "icons" / "hicolor"
        if icons_root.is_dir():
            for installed in icons_root.glob(f"*/apps/{_APP_ID}.png"):
                installed.unlink(missing_ok=True)

    def install_autostart(self) -> None:
        dest = _desktop_file(autostart=True)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(_desktop_content(autostart=True), encoding="utf-8")

    def uninstall_autostart(self) -> None:
        _desktop_file(autostart=True).unlink(missing_ok=True)

    def apply(self, mode: str) -> None:
        """Apply a system-registration mode: "app", "autostart", "all" or "none"."""
        if mode == "none":
            self.uninstall_app()
            self.uninstall_autostart()
            return
        if mode in ("app", "all"):
            self.install_app()
        if mode in ("autostart", "all"):
            self.install_autostart()


installer = Installer()
