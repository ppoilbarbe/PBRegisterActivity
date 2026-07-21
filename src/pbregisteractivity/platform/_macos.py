"""macOS platform services.

Reuses Linux's data directory, single-instance lock and executable
resolution as-is (POSIX behaviour is identical); only system registration
differs (an ``.app`` bundle instead of a ``.desktop`` file, a LaunchAgent
instead of an XDG autostart entry).
"""

import plistlib
import shutil
import subprocess
from pathlib import Path

from ._linux import (
    _APP_ID,
    _APP_NAME,
    _ICON_SOURCE,
    SingleInstance,
    SingleInstanceException,
    app_dir,
    executable_path,
)
from ._linux import Installer as _LinuxInstaller

__all__ = ["SingleInstance", "SingleInstanceException", "app_dir", "installer"]

_MACOS_BUNDLE_ID = f"net.cardolan.{_APP_ID}"


def _app_bundle() -> Path:
    return Path.home() / "Applications" / f"{_APP_NAME}.app"


def _launch_agent() -> Path:
    return Path.home() / "Library" / "LaunchAgents" / f"{_MACOS_BUNDLE_ID}.plist"


def _install_icon(resources_dir: Path) -> str | None:
    iconset = resources_dir / f"{_APP_ID}.iconset"
    icns = resources_dir / f"{_APP_ID}.icns"
    try:
        iconset.mkdir(parents=True, exist_ok=True)
        for size in (16, 32, 128, 256, 512):
            subprocess.run(
                [
                    "sips",
                    "-z",
                    str(size),
                    str(size),
                    str(_ICON_SOURCE),
                    "--out",
                    str(iconset / f"icon_{size}x{size}.png"),
                ],
                check=True,
                capture_output=True,
            )
            subprocess.run(
                [
                    "sips",
                    "-z",
                    str(size * 2),
                    str(size * 2),
                    str(_ICON_SOURCE),
                    "--out",
                    str(iconset / f"icon_{size}x{size}@2x.png"),
                ],
                check=True,
                capture_output=True,
            )
        subprocess.run(
            ["iconutil", "-c", "icns", str(iconset), "-o", str(icns)],
            check=True,
            capture_output=True,
        )
        return icns.name
    except (OSError, subprocess.CalledProcessError):
        icns.unlink(missing_ok=True)
        return None
    finally:
        shutil.rmtree(iconset, ignore_errors=True)


class Installer(_LinuxInstaller):
    def install_app(self) -> None:
        bundle = _app_bundle()
        macos_dir = bundle / "Contents" / "MacOS"
        resources_dir = bundle / "Contents" / "Resources"
        macos_dir.mkdir(parents=True, exist_ok=True)
        resources_dir.mkdir(parents=True, exist_ok=True)

        launcher = macos_dir / _APP_NAME
        launcher.write_text(
            f'#!/bin/sh\nexec "{executable_path()}" "$@"\n', encoding="utf-8"
        )
        launcher.chmod(0o755)

        icon_name = _install_icon(resources_dir)

        info_plist: dict[str, object] = {
            "CFBundleName": _APP_NAME,
            "CFBundleDisplayName": _APP_NAME,
            "CFBundleIdentifier": _MACOS_BUNDLE_ID,
            "CFBundleExecutable": _APP_NAME,
            "CFBundlePackageType": "APPL",
        }
        if icon_name:
            info_plist["CFBundleIconFile"] = icon_name
        with open(bundle / "Contents" / "Info.plist", "wb") as f:
            plistlib.dump(info_plist, f)

    def uninstall_app(self) -> None:
        shutil.rmtree(_app_bundle(), ignore_errors=True)

    def install_autostart(self) -> None:
        dest = _launch_agent()
        dest.parent.mkdir(parents=True, exist_ok=True)
        agent_plist = {
            "Label": _MACOS_BUNDLE_ID,
            "ProgramArguments": [executable_path()],
            "RunAtLoad": True,
        }
        with open(dest, "wb") as f:
            plistlib.dump(agent_plist, f)
        subprocess.run(["launchctl", "load", "-w", str(dest)], check=False)

    def uninstall_autostart(self) -> None:
        dest = _launch_agent()
        if dest.is_file():
            subprocess.run(["launchctl", "unload", "-w", str(dest)], check=False)
            dest.unlink(missing_ok=True)


installer = Installer()
