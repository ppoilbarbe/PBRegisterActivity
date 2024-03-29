#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main program for PBRegisterActivity
"""

import fcntl
import os
import sys

# pylint: disable=no-name-in-module
from PyQt5.QtCore import QLibraryInfo, QLocale, QTranslator
from PyQt5.QtWidgets import QApplication

from pbregisteractivity.mainwindow import MainWindow
from pbregisteractivity.parameters import parameters
from pbregisteractivity.utils import handle_gui_exception


class SingleInstanceException(BaseException):
    """raised when an instance of program is active"""


class SingleInstance:
    def __init__(self, lock_file):
        self.initialized = False
        self.lockfile = lock_file
        self.fp = open(self.lockfile, "w")
        self.fp.flush()
        try:
            fcntl.lockf(self.fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except IOError:
            print(
                "Application déjà en cours de fonctionnement ailleurs et "
                "pas forcément sur ce poste,",
                "fermeture.",
                file=sys.stderr,
            )
            raise SingleInstanceException()
        self.initialized = True

    def __del__(self):
        if not self.initialized:
            return
        fcntl.lockf(self.fp, fcntl.LOCK_UN)
        # os.close(self.fp)
        if os.path.isfile(self.lockfile):
            os.unlink(self.lockfile)


# noinspection PyArgumentList
def translate_stock_widgets(app: QApplication) -> None:
    """
    Set QT standard internal strings translated
    :param app: Application
    :return: None
    """
    locale_name = QLocale.system().name()
    qt_name = "qt_{0}".format(locale_name)
    translator = QTranslator()
    translator.load(qt_name, QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)


def main():
    try:
        locked = SingleInstance(parameters.unique_instance_lock_file)
    except SingleInstanceException:
        sys.exit(1)

    app = QApplication(sys.argv)
    translate_stock_widgets(app)
    mw = MainWindow()
    mw.main()
    sys.excepthook = handle_gui_exception
    exitcode = app.exec()
    del locked
    sys.exit(exitcode)


if __name__ == "__main__":
    main()
