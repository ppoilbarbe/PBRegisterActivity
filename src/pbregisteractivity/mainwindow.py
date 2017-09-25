#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

"""
Implémente le comportement de la fenêtre printipale.
Fait aussi office de programme principal de l'interface graphique.
"""

# Tested with PYTHON 3.5. Not compatible with Python 2.x

from PyQt5.QtCore import QByteArray, QDateTime, QTimer, Qt
from PyQt5.QtWidgets import QDialog, QMainWindow, QMessageBox

from .activity import Activity, activities
from .custom_widgets import QActivityListWidgetItem
from .parameters import parameters
from .specifyrange import SpecifyRange
from .timeplots import TimePlots
from .about import About
from .ui.ui_mainwindow import Ui_MainWindow
from .utils import to_string

__version__ = "0.0.5"


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self._title_normal = False
        self._timer = QTimer(self)
        self.setupUi(self)
        self.more_ui()

    def main(self):
        self.restore_window_state()
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

        # noinspection PyUnresolvedReferences
        self._timer.timeout.connect(self.check_window)

        self._timer.setInterval(1000)
        self._timer.start()

        self.set_now()

        self.fill_activity_list()

    @staticmethod
    def program_version():
        return "{0} - {1}".format(parameters.application_name, __version__)

    def change_title(self, special_text=None):
        if special_text is None or self.windowState() & Qt.WindowMinimized != Qt.WindowMinimized:
            if not self._title_normal:
                self.setWindowTitle(self.program_version())
                self._title_normal = True
        else:
            self.setWindowTitle(special_text)
            self._title_normal = False

    def restore_window_state(self):
        data = parameters.get_window_geometry()
        if data != "":
            self.restoreGeometry(QByteArray.fromBase64(data.encode("utf-8")))

        data = parameters.get_window_state()
        if data != "":
            self.restoreState(QByteArray.fromBase64(data.encode("utf-8")))

    def save_window_state(self):
        parameters.set_window_geometry(self.saveGeometry().toBase64())
        parameters.set_window_state(self.saveState().toBase64())

    def check_window(self):
        has_name = len(self.current_activity_name()) != 0
        date_is_ok = self.show_time()
        self.actionSave.setEnabled(activities.modified())
        self.actionRegister.setEnabled(has_name and date_is_ok)
        self.tbForceAdd.setEnabled(has_name and date_is_ok)

    def set_list_actions_enabled(self, selected_count=0):
        self.actionRemove.setEnabled(selected_count != 0)
        self.actionEdit.setEnabled(selected_count == 1)
        self.actionSwapActivity.setEnabled(selected_count == 1)

    def show_time(self):
        end_date = self.end_date()
        diff = int(self.start_date().secsTo(end_date))
        if diff < 0:
            txt = "--:--:--"
        else:
            (h, m) = divmod(diff, 3600)
            (m, s) = divmod(m, 60)
            txt = "{:02d}:{:02d}:{:02d}".format(h, m, s)
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
        selected_count = len(selected)
        if selected_count != 1:
            self.txtDescription.clear()
            # noinspection PyUnresolvedReferences
            self.statusBar.clearMessage()
        else:
            text = selected[0].value().as_html()
            self.txtDescription.setHtml(text)
            # noinspection PyUnresolvedReferences
            self.statusBar.showMessage(selected[0].statusTip())
        self.set_list_actions_enabled(selected_count=selected_count)
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
        self.save_window_state()
        parameters.write()
        activities.write()
