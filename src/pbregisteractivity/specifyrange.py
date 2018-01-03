#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
Dialogue utilisé pour ajouter une plage d'activité manuellement
"""

# Tested with PYTHON 3.5. Not compatible with Python 2.x

from PyQt5.QtCore import QTime, pyqtSlot
from PyQt5.QtWidgets import QDialog, QDialogButtonBox

from .activity import Activity, activities
from .utils import to_string
from .ui.ui_specifyrange import Ui_SpecifyRange


# noinspection PyAbstractClass
class SpecifyRange(QDialog, Ui_SpecifyRange):
    def __init__(self, activity, title, modify=False):
        super().__init__()
        self._activity = activity
        self._modify = modify
        self.setupUi(self)
        self.setWindowTitle(title)
        self.lblTitle.setText(title)
        self.edtName.setText(activity.name)
        self.dteStart.setDateTime(activity.start)
        self.edtComment.setPlainText(activity.comment)
        d = activity.duration
        self.sbDayDuration.setValue(d.days)
        self.timeDuration.setTime(QTime(0, 0, 0).addSecs(d.seconds))
        self.check_window()

        self.edtName.textChanged.connect(self.check_window)
        self.sbDayDuration.valueChanged.connect(self.duration_changed)
        self.timeDuration.dateTimeChanged.connect(self.duration_changed)
        self.dteStart.dateTimeChanged.connect(self.duration_changed)
        self.dteEnd.dateTimeChanged.connect(self.end_changed)
        self._in_update = False
        self.duration_changed()

    def name(self):
        return to_string(self.edtName.text())

    def start_date(self):
        return self.dteStart.dateTime()

    def end_date(self):
        return self.dteEnd.dateTime()

    def secs_duration(self):
        return self.start_date().secsTo(self.end_date())

    def days_duration(self):
        result, _ = divmod(self.secs_duration(), 86400)
        return result

    def check_window(self):
        valid_name = self.name() != ""
        valid_end = self.start_date() < self.end_date() and self.days_duration() <= self.sbDayDuration.maximum()
        self.lblEndWarning.setVisible(not valid_end)
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(valid_name and valid_end)

    def duration_changed(self):
        if self._in_update:
            return
        self._in_update = True
        days = self.sbDayDuration.value()
        time = self.timeDuration.time()
        duration = days * 86400 + time.hour() * 3600 + time.minute() * 60 + time.second()
        self.dteEnd.setDateTime(self.start_date().addSecs(duration))
        self.check_window()
        self._in_update = False

    def end_changed(self):
        if self._in_update:
            return
        self._in_update = True
        duration = self.secs_duration()
        if duration > 0:
            days, seconds = divmod(duration, 86400)
            self.sbDayDuration.setValue(days)
            self.timeDuration.setTime(QTime(0, 0, 0).addSecs(seconds))
        self.check_window()
        self._in_update = False

    @pyqtSlot()
    def accept(self):
        name = self.name()
        start = self.start_date().toString("yyyyMMddThhmmss")
        end = self.end_date().toString("yyyyMMddThhmmss")
        comment = self.edtComment.toPlainText()
        if self._modify:
            self._activity.name = name
            self._activity.start = start
            self._activity.end = end
            self._activity.comment = comment
        else:
            activities.add(Activity(name,
                                    start,
                                    end,
                                    comment))
        return super().accept()
