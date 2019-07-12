# -*- coding: utf-8 -*-
"""
Dialogue utilisé pour ajouter une plage d'activité manuellement
"""

# Tested with PYTHON 3.5. Not compatible with Python 2.x

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .parameters import parameters
from .ui.ui_prefs import Ui_Prefs


# noinspection PyAbstractClass
class Prefs(QDialog, Ui_Prefs):
    WINDOW_NAME = "prefs"

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.spinDayDuration.setValue(parameters.day_duration)
        self.spinMisc.setValue(parameters.misc_duration)
        self.cbToTray.setChecked(parameters.minimize_to_tray)
        self.cbAutoSave.setChecked(parameters.auto_save)
        parameters.restore_window_state(self)

    def save_data(self):
        parameters.day_duration = self.spinDayDuration.value()
        parameters.misc_duration = self.spinMisc.value()
        parameters.minimize_to_tray = self.cbToTray.isChecked()
        parameters.auto_save = self.cbAutoSave.isChecked()

    def window_is_about_to_be_closed(self):
        parameters.save_window_state(self)

    def closeEvent(self, event):
        self.window_is_about_to_be_closed()
        event.accept()

    @pyqtSlot()
    def reject(self):
        self.window_is_about_to_be_closed()
        return super().reject()

    @pyqtSlot()
    def accept(self):
        self.save_data()
        self.window_is_about_to_be_closed()
        return super().accept()
