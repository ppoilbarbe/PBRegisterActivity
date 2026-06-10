"""Répertoire de données applicatif selon la plateforme.

- Linux / macOS : ~/.pbregisteractivity/
- Windows       : %APPDATA%\\pbregisteractivity\\
"""

import os
import sys
from pathlib import Path

_APP_NAME = "pbregisteractivity"


def app_dir() -> Path:
    """Retourne le répertoire de données de l'application, en le créant si besoin."""
    if sys.platform == "win32":
        base = os.environ.get("APPDATA")
        p = (
            Path(base) / _APP_NAME
            if base
            else Path.home() / "AppData" / "Roaming" / _APP_NAME
        )
    else:
        p = Path.home() / f".{_APP_NAME}"
    p.mkdir(parents=True, exist_ok=True)
    return p
