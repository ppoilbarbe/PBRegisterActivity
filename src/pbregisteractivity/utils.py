#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import os
import sys
import traceback
from datetime import timedelta

from PyQt5.QtWidgets import QApplication, QMessageBox

try:
    import pwd
except ImportError:
    import getpass

    pwd = None


def handle_gui_exception(exc_type, exc_value, exc_traceback):
    t = traceback.format_exception(exc_type, exc_value, exc_traceback)
    print(''.join(t), flush=True, file=sys.stderr)
    err_msg = ''.join(t[-10:])
    if len(t) > 10:
        err_msg = "...\n" + err_msg
    err_msg += '\nContinuer quand même ?'
    # Here collecting traceback and some log files to be sent for debugging.
    # But also possible to handle the error and continue working.
    # noinspection PyArgumentList
    if QMessageBox.critical(None,
                            "ERREUR - Exception non capturée",
                            err_msg,
                            buttons=QMessageBox.Yes | QMessageBox.No,
                            defaultButton=QMessageBox.No) != QMessageBox.Yes:
        # noinspection PyArgumentList
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
        s = ("{0:1.8f}".format(value)).rstrip('0')
        if s[-1] == '.':
            s += '0'
        return s

    if isinstance(value, int):
        return str(value)

    for encoding in ('ascii', 'utf8', 'iso-8859-15'):
        try:
            return str(value, encoding=encoding)
        except (UnicodeDecodeError, UnicodeEncodeError):
            pass
    return str(value, encoding='utf8', errors='replace')


def format_duration(duration: float) -> str:
    """
    Format a duration expressed in decimal seconds as a time in
    decimal hours and duratons H:M:S
    :param duration: In seconds
    :return: Formatted string
    """
    t = timedelta(seconds=duration)
    d = t.days
    h, s = divmod(t.seconds, 3600)
    m, s = divmod(s, 60)
    dstr = "{}j ".format(d) if d > 0 else ""
    return "{:1.2f}h - {}{:02d}:{:02d}:{:02d}".format(duration / 3600.0,
                                                      dstr,
                                                      h,
                                                      m,
                                                      s)
