#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

"""
Enregistre l'activité
"""

# Tested with PYTHON 3.5. Not compatible with Python 2.x

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidgetItem

from .activity import Activity


class QActivityListWidgetItem(QListWidgetItem):
    def __init__(self, value: Activity):
        super().__init__()
        start = value.start.strftime("%Y/%m/%d %H:%M:%S")
        end = value.end.strftime("%Y/%m/%d %H:%M:%S")
        duration = str(value.end - value.start)
        txt = "{name} ({start} - {duration})".format(
            name=value.name,
            start=start,
            duration=duration,
        )
        self.setText(txt)
        txt = "Début: {start}<br>Fin: {end}<br>Durée: {duration}".format(
            start=start,
            end=end,
            duration=duration)
        self.setToolTip(txt)
        txt = "{name} - Début: {start}; Fin: {end}; Durée: {duration}".format(
            name=value.name,
            start=start,
            end=end,
            duration=duration)
        self.setStatusTip(txt)
        self.setData(Qt.UserRole, value)

    def value(self):
        return self.data(Qt.UserRole)
