#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

"""
Implémente le comportement de la fenêtre printipale.
Fait aussi office de programme principal de l'interface graphique.
"""

# Tested with PYTHON 3.5. Not compatible with Python 2.x

from PyQt5.QtCore import QDateTime, QTimer, Qt
from PyQt5.QtWidgets import QDialog, QMainWindow, QMessageBox, QLCDNumber

from datetime import datetime, timedelta
from .about import About
from .activity import Activity, activities
from .custom_widgets import QActivityListWidgetItem
from .parameters import parameters
from .specifyrange import SpecifyRange
from .timeplots import TimePlots
from .ui.ui_mainwindow import Ui_MainWindow
from .utils import to_string, format_duration
from .version import __version__ as version


class MainWindow(QMainWindow, Ui_MainWindow):
    WINDOW_NAME = "main_window"
    def __init__(self):
        super().__init__()
        self._title_normal = False
        self._tick_count = 0
        self._timer = QTimer(self)
        self.setupUi(self)
        self.more_ui()

    def main(self):
        parameters.restore_window_state(self)
        self.show()

    def more_ui(self):
        self.change_title()
        self.actionQuit.triggered.connect(self.close)
        self.actionRegister.triggered.connect(self.handle_register_action)
        self.actionCancel.triggered.connect(self.handle_cancel_action)
        self.actionRemove.triggered.connect(self.handle_remove_action)
        self.actionEdit.triggered.connect(self.handle_edit_action)
        self.actionSave.triggered.connect(self.handle_save_action)
        self.actionSwapActivity.triggered.connect(self.handle_swap_activity_action)
        self.actionAbout.triggered.connect(self.handle_about_action)
        self.actionExtract.triggered.connect(self.handle_extract_action)

        self.tbForceAdd.clicked.connect(self.handle_force_add_action)

        self.dteStart.dateTimeChanged.connect(self.check_window)
        self.cbbActivities.currentTextChanged.connect(self.check_window)
        self.listHistory.itemSelectionChanged.connect(self.handle_history_selected_action)
        self.listHistory.doubleClicked.connect(self.handle_edit_action)
        self.edtFilter.textChanged.connect(self.handle_filter_changed)

        self.lcdDayTime = QLCDNumber(self.layoutWidget1)
        self.lcdDayTime.setSmallDecimalPoint(False)
        self.lcdDayTime.setDigitCount(5)
        self.lcdDayTime.setSegmentStyle(QLCDNumber.Flat)
        self.lcdDayTime.setObjectName("lcdDayTime")
        self.lcdDayTime.setToolTip("Cumul du temps sur la journée")
        self.statusBar.addPermanentWidget(self.lcdDayTime)


        # noinspection PyUnresolvedReferences
        self._timer.timeout.connect(self.handle_timer)

        self._timer.setInterval(1000)
        self._timer.start()

        self.set_now()

        self.fill_activity_list()

    @staticmethod
    def program_version():
        return "{0} - {1}".format(parameters.application_name, version)

    def change_title(self, special_text=None):
        if special_text is None or self.windowState() & Qt.WindowMinimized != Qt.WindowMinimized:
            if not self._title_normal:
                self.setWindowTitle(self.program_version())
                self._title_normal = True
        else:
            self.setWindowTitle(special_text)
            self._title_normal = False

    def check_window(self, with_day_time=True):
        has_name = len(self.current_activity_name()) != 0
        date_is_ok = self.show_time()
        self.actionSave.setEnabled(activities.modified())
        self.actionRegister.setEnabled(has_name and date_is_ok)
        self.tbForceAdd.setEnabled(has_name and date_is_ok)
        if with_day_time:
            self.update_day_time()

    def set_list_actions_enabled(self, selected_count=0):
        self.actionRemove.setEnabled(selected_count != 0)
        self.actionEdit.setEnabled(selected_count == 1)
        self.actionSwapActivity.setEnabled(selected_count == 1)

    def show_time(self):
        end_date = self.end_date()
        diff = int(self.start_date().secsTo(end_date))
        txt = self._time_text(diff)
        name = self.current_activity_name()
        if name == "":
            name = "<pas de nom>"
        self.change_title(special_text="{0} - {1}".format(txt, name))
        self.lcdDuration.display(txt)
        txt = self.end_date().toString("yyyy/MM/dd hh:mm:ss")
        lbl = self.lblEndText
        lbl.setText(txt)
        ok = False
        if diff >= 90 * 3600:
            style = '{name} {{' \
                    'color:{fg}; ' \
                    'background-color:{bg}; ' \
                    'font-weight: bold;' \
                    '}}'
            style = style.format(name=lbl.metaObject().className(),
                                 fg="#FFFF00",
                                 bg="#FF0000"
                                 )
        elif diff < 0:
            style = '{name} {{' \
                    'color:{fg}; ' \
                    'background-color:{bg}; ' \
                    'font-weight: bold;' \
                    '}}'
            style = style.format(name=lbl.metaObject().className(),
                                 fg="#000000",
                                 bg="#F3F346"
                                 )
        else:
            style = ""
            ok = True
        lbl.setStyleSheet(style)
        return ok

    def update_day_time(self):
        current_diff = self.start_date().secsTo(self.end_date())
        today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
        for x in activities.pack_durations(start=today, end=today + timedelta(days=1)).values():
            current_diff += x['duration']
        self.lcdDayTime.display(self._time_text(current_diff, with_seconds=False))
        self._tick_count = 0


    def set_now(self):
        self.dteStart.setDateTime(QDateTime.currentDateTime())
        self.edtComment.clear()
        self.cbbActivities.clearEditText()
        self.cbbActivities.setFocus()
        self.check_window()

    def start_date(self):
        return self.dteStart.dateTime()

    @staticmethod
    def end_date():
        return QDateTime.currentDateTime()

    def current_activity_name(self):
        return to_string(self.cbbActivities.currentText()).strip()

    def get_activity_from_window(self):
        return Activity(self.current_activity_name(),
                        self.start_date().toString("yyyyMMddThhmmss"),
                        self.end_date().toString("yyyyMMddThhmmss"),
                        self.edtComment.toPlainText().strip())

    def do_add_activity(self):
        if self.current_activity_name() != "":
            activities.add(self.get_activity_from_window())
            return True
        return False

    def fill_activity_list(self):
        oldtxt = self.cbbActivities.currentText()
        self.cbbActivities.clear()
        self.cbbActivities.addItems(activities.actvitiy_names())
        self.cbbActivities.setCurrentText(oldtxt)
        self.set_list_actions_enabled()
        lst = self.listHistory
        lst.clear()
        for x in activities.all_activities(recent_first=True):
            lst.addItem(QActivityListWidgetItem(x))

    @staticmethod
    def show_selection(selected):
        count = len(selected)
        if count == 0:
            return "Pas de sélection", None, None
        if count == 1:
            return ("Plage enregistrée sélectionnée",
                    selected[0].value().as_html(),
                    selected[0].statusTip())
        duration = 0
        for x in selected:
            duration += x.value().seconds_duration
        dtxt = format_duration(duration)
        txt = "<p>{} plages sélectionnées.</p><p>Durée cumulée: <b>{}</b></p>".format(count, dtxt)
        return ("Plages enregistrées sélectionnées",
                txt,
                dtxt)

    def handle_timer(self):
        self._tick_count += 1
        self.check_window(with_day_time=self._tick_count >= 30)

    def handle_filter_changed(self):
        txt = self.edtFilter.text().lower()
        for index in range(self.listHistory.count()):
            x = self.listHistory.item(index)
            hidden = txt != "" and txt not in x.value().name.lower()
            x.setHidden(hidden)
            if hidden:
                x.setSelected(False)

    def handle_register_action(self):
        self.do_add_activity()
        self.fill_activity_list()
        self.set_now()

    def handle_swap_activity_action(self):
        selected = self.listHistory.selectedItems()
        if len(selected) != 1:
            return
        selected = selected[0].value()
        if self.do_add_activity():
            self.fill_activity_list()
            self.set_now()
        self.edtComment.setPlainText(selected.comment)
        self.cbbActivities.setCurrentText(selected.name)

    def handle_remove_action(self):
        selected = self.listHistory.selectedItems()
        if len(selected) < 2:
            msg = "la plage sélectionnée"
        else:
            msg = "les {0} plages sélectionnées".format(len(selected))
        msg = "Êtes-vous sûr de vouloir supprimer {0} ?".format(msg)
        reply = QMessageBox.question(
            self,
            "Suppression de plages",
            msg,
            buttons=QMessageBox.Yes | QMessageBox.No,
            defaultButton=QMessageBox.No)
        if reply == QMessageBox.Yes:
            for x in selected:
                activities.remove(x.value())
            self.fill_activity_list()
            self.check_window()

    def handle_edit_action(self):
        selected = self.listHistory.selectedItems()
        if len(selected) != 1:
            return
        modaldlg = SpecifyRange(selected[0].value(), "Modification d'une activité", modify=True)
        if modaldlg.exec_() != QDialog.Rejected:
            self.fill_activity_list()

    # noinspection PyMethodMayBeStatic
    def handle_save_action(self):
        activities.write()

    def handle_history_selected_action(self):
        selected = self.listHistory.selectedItems()
        what, text, status = self.show_selection(selected)
        self.lblSelected.setText(what)
        if text:
            self.txtSelected.setHtml(text)
        else:
            self.txtSelected.clear()
        if status:
            self.statusBar.showMessage(status)
        else:
            self.statusBar.clearMessage()
        self.set_list_actions_enabled(selected_count=len(selected))
        self.check_window()

    def handle_cancel_action(self):
        self.set_now()
        self.restore_window_state()

    def handle_force_add_action(self):
        modaldlg = SpecifyRange(self.get_activity_from_window(), "Création d'une activité")
        if modaldlg.exec_() != QDialog.Rejected:
            self.cbbActivities.clearEditText()
            self.edtComment.clear()
            self.fill_activity_list()

    def handle_about_action(self):
        modaldlg = About(self.program_version())
        modaldlg.exec_()

    # noinspection PyMethodMayBeStatic
    def handle_extract_action(self):
        modaldlg = TimePlots()
        modaldlg.exec_()

    def closeEvent(self, event):
        self._timer.stop()
        if self.current_activity_name() != "":
            # noinspection PyCallByClass
            reply = QMessageBox.question(
                self,
                "Question de fin",
                "Sauvegarder la dernière activité avant de quitter",
                buttons=QMessageBox.Yes | QMessageBox.No,
                defaultButton=QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.do_add_activity()
        event.accept()
        parameters.save_window_state(self)
        parameters.write()
        activities.write()

    @staticmethod
    def _time_text(seconds, with_seconds=True):
        if with_seconds:
            length = 8
        else:
            length = 5
        if seconds < 0:
            txt = "--:--:--"
        else:
            (h, m) = divmod(seconds, 3600)
            (m, s) = divmod(m, 60)
            txt = "{:02d}:{:02d}:{:02d}".format(int(h), int(m), int(s))
        return txt[:length]
