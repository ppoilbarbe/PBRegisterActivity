"""Bundled icon files used by the Qt UI."""

from pathlib import Path

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap

DIR = Path(__file__).parent


def icon(name: str, size: int | None = None) -> QIcon:
    """Build a QIcon from an icon file in this directory.

    All bundled icons are square, so a single side length is enough.
    """
    qsize = QSize(size, size) if size is not None else QSize()
    result = QIcon()
    result.addFile(str(DIR / name), qsize, QIcon.Mode.Normal, QIcon.State.Off)
    return result


def pixmap(name: str) -> QPixmap:
    """Load a QPixmap from an icon file in this directory."""
    return QPixmap(str(DIR / name))
