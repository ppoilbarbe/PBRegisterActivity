#!/usr/bin/env python3

"""
Main program for PBRegisterActivity
"""

import sys

from PySide6.QtCore import QLibraryInfo, QLocale, QTranslator
from PySide6.QtWidgets import QApplication

from pbregisteractivity.activity import activities
from pbregisteractivity.mainwindow import MainWindow
from pbregisteractivity.parameters import parameters
from pbregisteractivity.platform.lock import SingleInstance, SingleInstanceException
from pbregisteractivity.resources import icon
from pbregisteractivity.utils import handle_gui_exception


def translate_stock_widgets(app: QApplication) -> None:
    locale_name = QLocale.system().name()
    qt_name = f"qt_{locale_name}"
    translator = QTranslator()
    translator.load(
        qt_name, QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)
    )
    app.installTranslator(translator)


def main():
    try:
        locked = SingleInstance(parameters.unique_instance_lock_file)
    except SingleInstanceException:
        sys.exit(1)

    activities.load(parameters.activity_file)

    app = QApplication(sys.argv)
    app.setWindowIcon(icon("pbregisteractivity.png", size=128))
    translate_stock_widgets(app)
    mw = MainWindow()
    mw.main()
    sys.excepthook = handle_gui_exception
    exitcode = app.exec()
    del locked
    sys.exit(exitcode)


if __name__ == "__main__":
    main()
