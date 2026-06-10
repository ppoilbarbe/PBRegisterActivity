#!/usr/bin/env python3

"""
Main program for PBRegisterActivity
"""

import sys

from PySide6.QtCore import QLibraryInfo, QLocale, QSize, QTranslator
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

import pbregisteractivity.ui  # registers Qt resources (resources_rc) # noqa: F401
from pbregisteractivity.activity import activities
from pbregisteractivity.mainwindow import MainWindow
from pbregisteractivity.parameters import parameters
from pbregisteractivity.platform.lock import SingleInstance, SingleInstanceException
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
    app_icon = QIcon()
    app_icon.addFile(
        ":/images/icons/128x128/obj_hal9000.png",
        QSize(128, 128),
        QIcon.Mode.Normal,
        QIcon.State.Off,
    )
    app.setWindowIcon(app_icon)
    translate_stock_widgets(app)
    mw = MainWindow()
    mw.main()
    sys.excepthook = handle_gui_exception
    exitcode = app.exec()
    del locked
    sys.exit(exitcode)


if __name__ == "__main__":
    main()
