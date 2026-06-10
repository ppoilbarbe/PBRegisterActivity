import os
import sys
import traceback
from datetime import timedelta

from PySide6.QtWidgets import QApplication, QMessageBox

from .parameters import parameters

try:
    import pwd
except ImportError:
    import getpass

    pwd = None


def handle_gui_exception(exc_type, exc_value, exc_traceback):
    t = traceback.format_exception(exc_type, exc_value, exc_traceback)
    print("".join(t), flush=True, file=sys.stderr)
    err_msg = "".join(t[-10:])
    if len(t) > 10:
        err_msg = "...\n" + err_msg
    err_msg += "\nContinuer quand même ?"
    if (
        QMessageBox.critical(
            None,
            "ERREUR - Exception non capturée",
            err_msg,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )
        != QMessageBox.StandardButton.Yes
    ):
        QApplication.quit()


def username():
    if pwd:
        return pwd.getpwuid(os.geteuid()).pw_name
    return getpass.getuser()


def to_string(value):
    if value is None:
        return None

    if isinstance(value, str):
        return value

    if isinstance(value, float):
        s = (f"{value:1.8f}").rstrip("0")
        if s[-1] == ".":
            s += "0"
        return s

    if isinstance(value, int):
        return str(value)

    for encoding in ("ascii", "utf8", "iso-8859-15"):
        try:
            return str(value, encoding=encoding)
        except (UnicodeDecodeError, UnicodeEncodeError):
            pass
    return str(value, encoding="utf8", errors="replace")


def format_duration(duration: float, with_partial_day: bool = False) -> str:
    """
    Format a duration expressed in decimal seconds as a time in
    decimal hours and durations H:M:S
    :param duration: In seconds
    :return: Formatted string
    """
    secs_by_day = parameters.day_duration * 3600.0
    d = int(duration // secs_by_day)
    t = timedelta(seconds=duration - d * secs_by_day)
    assert t.days == 0
    h, s = divmod(t.seconds, 3600)
    m, s = divmod(s, 60)
    dstr = f"{d}j " if d > 0 else ""
    partial_day = f" - {duration / secs_by_day:1.2f}j" if with_partial_day else ""
    return f"{duration / 3600.0:1.2f}h - {dstr}{h:02d}:{m:02d}:{s:02d}{partial_day}"
