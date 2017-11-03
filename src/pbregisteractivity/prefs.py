#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
Dialogue utilisé pour ajouter une plage d'activité manuellement
"""

# Tested with PYTHON 3.5. Not compatible with Python 2.x

import os
import csv
import html
import re
from datetime import date, timedelta
from io import StringIO

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.dates import DateFormatter, DayLocator, HourLocator
from matplotlib.figure import Figure

from .activity import activities
from .parameters import parameters
from .ui.ui_prefs import Ui_Prefs
from .utils import format_duration


# noinspection PyAbstractClass
class Prefs(QDialog, Ui_Prefs):
    WINDOW_NAME = "prefs"

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.spinDayDuration.setValue(parameters.day_duration)
        parameters.restore_window_state(self)


    def save_data(self):
        parameters.day_duration = self.spinDayDuration.value()

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
