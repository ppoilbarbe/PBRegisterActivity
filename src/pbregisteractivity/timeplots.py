# -*- coding: utf-8 -*-
"""
Dialogue utilisé pour ajouter une plage d'activité manuellement
"""

# Tested with PYTHON 3.5. Not compatible with Python 2.x

import csv
import html
import os
import re
from datetime import date, timedelta
from io import StringIO

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.dates import DateFormatter, DayLocator, HourLocator
from matplotlib.figure import Figure
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox

from .activity import activities
from .parameters import parameters
from .ui.ui_timeplots import Ui_TimePlots
from .utils import format_duration


# noinspection PyAbstractClass
class TimePlots(QDialog, Ui_TimePlots):
    PLOT_TIMELINES = 0
    PLOT_PIECHART = 1
    PLOT_TEXT = 2
    WINDOW_NAME = "graphs"
    PARAM_FULL_CVS = "full_csv"

    # noinspection PyTypeChecker
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        today = date.today()
        self.deStart.setDate(today - timedelta(days=today.weekday()))
        self.deEnd.setDate(today)

        self.deStart.dateChanged.connect(self.check_window)
        self.deEnd.dateChanged.connect(self.check_window)

        self.cbCsvFull.stateChanged.connect(self.check_window)

        self.btnTimeLines.clicked.connect(self.handle_timelines)
        self.btnPieChart.clicked.connect(self.handle_piechart)
        self.btnTextOutput.clicked.connect(self.handle_text_output)

        self.btnPrevWeek.clicked.connect(self.handle_previous_week)
        self.btnNextWeek.clicked.connect(self.handle_next_week)
        self.btnToday.clicked.connect(self.handle_today)
        self.btnWorkWeek.clicked.connect(self.handle_workweek)

        self.btnHtmlSave.clicked.connect(self.handle_savehtml)
        self.btnCsvSave.clicked.connect(self.handle_savecsv)

        self.plot_buttons = [self.btnTimeLines, self.btnPieChart, self.btnTextOutput]

        self._mpl_canvas = [None] * 3
        self._mpl_toolbar = [None] * 3
        self._figure = [None] * 3
        for plotid, layout in [
            [self.PLOT_TIMELINES, self.layoutTimeLines],
            [self.PLOT_PIECHART, self.layoutPieChart],
        ]:
            self._figure[plotid] = Figure()
            self._mpl_canvas[plotid] = FigureCanvas(self._figure[plotid])
            self._mpl_toolbar[plotid] = NavigationToolbar(
                self._mpl_canvas[plotid], self
            )
            layout.addWidget(self._mpl_canvas[plotid])
            layout.addWidget(self._mpl_toolbar[plotid])
        self.lblDurations.setText(
            "Durée journalière: {}h; Divers=Durée<{}min".format(
                parameters.day_duration, parameters.misc_duration
            )
        )
        self.switch_panel(None)
        self.cbCsvFull.setChecked(parameters.app_get_bool(self.PARAM_FULL_CVS))
        parameters.restore_window_state(self)

    def check_window(self):
        for x in self.plot_buttons:
            if x.isChecked():
                x.click()
                break

    def handle_today(self):
        self.set_dates(date.today(), 0)

    def handle_workweek(self):
        refdate = date.today()
        self.set_dates(refdate - timedelta(days=refdate.weekday()), 4)

    def handle_previous_week(self):
        self.move_dates(timedelta(days=-7))

    def handle_next_week(self):
        self.move_dates(timedelta(days=7))

    def set_dates(self, start, days):
        self.deStart.setDate(start)
        self.deEnd.setDate(start + timedelta(days=days))
        self.check_window()

    def move_dates(self, delta):
        # Ensure delta is in days
        tmpdelta = timedelta(days=delta.days)
        refdate = self.deStart.dateTime().toPyDateTime()
        duration = self.deEnd.dateTime().toPyDateTime() - refdate
        self.set_dates(refdate + tmpdelta, duration.days)

    def handle_timelines(self):
        self.switch_panel(self.PLOT_TIMELINES)
        start, end = self.get_date_range()
        what = activities.pack_by_name(start=start, end=end)
        plt = self.new_plot(self.PLOT_TIMELINES)

        duration = 0.0

        if len(what) > 0:
            plt.xaxis.set_major_locator(DayLocator())
            plt.xaxis.set_major_formatter(DateFormatter("%b-%d"))
            plt.xaxis.set_minor_locator(HourLocator(byhour=(8, 10, 12, 14, 16, 18, 20)))
            ylabels = []
            y = []
            datemin = None
            datemax = None
            for k, v in what.items():
                ylabels.append(k)
                y.append(len(ylabels))
                duration = sum([x.seconds_duration for x in v], duration)
                x1 = [x.start for x in v]
                x2 = [x.end for x in v]
                tmp = min(x1)
                if datemin is None or tmp < datemin:
                    datemin = tmp
                tmp = max(x1)
                if datemax is None or tmp > datemax:
                    datemax = tmp
                plt.hlines([y[-1]] * len(x1), x1, x2, lw=2, color="red")
            plt.set_ylim(len(ylabels) + 0.5, 0.5)
            plt.set_yticks(y)
            plt.set_yticklabels(ylabels)
            datemin -= timedelta(hours=4.0)
            datemax += timedelta(hours=4.0)
            plt.xaxis_date()
            for x in plt.xaxis.get_ticklabels():
                x.set_rotation(45)
                x.set_horizontalalignment("right")
            plt.set_xlim(left=datemin, right=datemax)
            plt.grid(which="major", axis="x", color="black", linestyle="dashed")
            plt.grid(
                which="minor", axis="x", color="black", alpha=0.6, linestyle="dotted"
            )
            self._figure[self.PLOT_TIMELINES].tight_layout()
        self.plot_title(self.PLOT_TIMELINES, duration=duration)
        # refresh canvas
        self._mpl_canvas[self.PLOT_TIMELINES].draw()

    def handle_piechart(self):
        self.switch_panel(self.PLOT_PIECHART)
        start, end = self.get_date_range()
        what = activities.pack_durations(start=start, end=end)
        labels = []
        values = []
        miscelaneous = 0.0
        duration = 0.0
        for k, v in what.items():
            d = v["duration"]
            duration += d
            if d < parameters.misc_duration * 60:
                miscelaneous += d
            else:
                labels.append("{} - {}".format(k, format_duration(d)))
                values.append(d)
        if miscelaneous > 0:
            labels.append("Divers - {}".format(format_duration(miscelaneous)))
            values.append(miscelaneous)

        plt = self.new_plot(self.PLOT_PIECHART)
        plt.pie(values, labels=labels, autopct="%1.1f%%")
        # Ratio d'aspect égal entre x et y ==> cercle
        plt.axis("equal")
        self.plot_title(self.PLOT_PIECHART, duration=duration)
        # Rafraichis le canevas
        self._mpl_canvas[self.PLOT_PIECHART].draw()

    def handle_text_output(self):
        self.switch_panel(self.PLOT_TEXT)
        start, end = self.get_date_range()
        what = activities.pack_durations(start=start, end=end)
        txt = ""
        strio = StringIO(newline="")
        partial = not self.cbCsvFull.isChecked()
        if partial:
            csvio = csv.DictWriter(
                strio,
                quoting=csv.QUOTE_ALL,
                fieldnames=["nom", "duree", "commentaires"],
            )
        else:
            csvio = csv.DictWriter(
                strio,
                quoting=csv.QUOTE_ALL,
                fieldnames=[
                    "nom",
                    "debut",
                    "fin",
                    "duree",
                    "duree_heures",
                    "commentaires",
                ],
            )
        csvio.writeheader()
        for k, v in what.items():
            txt += "<h1>{0}</h1>".format(html.escape(k))
            txt += "Durée: {}<br>".format(format_duration(v["duration"]))
            if len(v["comments"]) > 0:
                txt += "<ul>"
                for x in v["comments"]:
                    lines = [
                        html.escape(line)
                        for line in re.split("[\r\n]+", x)
                        if line != ""
                    ]
                    txt += "<li>{}</li>".format("<br>".join(lines))
                txt += "</ul>"
            if partial:
                csvio.writerow(
                    dict(
                        nom=k,
                        duree="{:1.2f}".format(v["duration"] / 3600.0),
                        commentaires="\n".join(v["comments"]),
                    )
                )
        if not partial:
            for k, v in activities.pack_by_name(start=start, end=end).items():
                for activity in v:
                    delta = activity.end - activity.start

                    csvio.writerow(
                        dict(
                            nom=k,
                            debut=activity.start.strftime("%Y-%m-%d %H:%M:%S"),
                            fin=activity.end.strftime("%Y-%m-%d %H:%M:%S"),
                            duree="{}".format(delta),
                            duree_heures="{:1.3f}".format(
                                delta.total_seconds() / 3600.0
                            ),
                            commentaires=activity.comment,
                        )
                    )

        self.edtHtml.setHtml(txt + "\n")
        self.edtCsv.setPlainText(strio.getvalue())

    def handle_savehtml(self):
        self.save_text(
            kind="HTML", ext=".html", text=self.edtHtml.toHtml(), param="html_dir"
        )

    def handle_savecsv(self):
        self.save_text(
            kind="CSV", ext=".csv", text=self.edtCsv.toPlainText(), param="csv_dir"
        )

    def switch_panel(self, what):
        self.frmTextOutput.setVisible(what == self.PLOT_TEXT)
        self.frmPieChart.setVisible(what == self.PLOT_PIECHART)
        self.frmTimeLines.setVisible(what == self.PLOT_TIMELINES)

    def new_plot(self, figure_id):
        fig = self._figure[figure_id]
        plt = fig.add_subplot(1, 1, 1)
        plt.clear()
        fig.set_facecolor("white")
        return plt

    def plot_title(self, figure_id, duration=0.0):
        txt = ""
        if duration > 0.0:
            txt = "Durées des activités ({})".format(format_duration(duration))
        fig = self._figure[figure_id]
        st = fig.suptitle(txt, fontsize="x-large")
        st.set_y(0.99)
        fig.subplots_adjust(top=0.85)

    def save_text(self, kind="Text", ext=".txt", text="", param=None):
        if text is None or len(text) == 0:
            return
        file_filter = "{0} (*{1});; Texte (*.txt);; Tous les fichiers (*)".format(
            kind, ext
        )
        directory = ""
        if param is not None:
            directory = parameters.app_get(param, default="")
        # noinspection PyArgumentList,PyCallByClass
        fn, flt = QFileDialog.getSaveFileName(
            self,
            caption="Sauvegarde au format {0}".format(kind),
            filter=file_filter,
            directory=directory,
            options=QFileDialog.DontResolveSymlinks,
        )
        if fn is None or fn == "":
            return
        try:
            with open(fn, "w") as f:
                f.write(text)
            # noinspection PyArgumentList,PyCallByClass
            QMessageBox.information(
                self,
                "SAUVEGARDE",
                "Fichier {} «{}» créé.".format(kind, fn),
                buttons=QMessageBox.Ok,
            )
            if param is not None:
                parameters.app_set(param, os.path.dirname(fn))
        except IOError as e:
            # noinspection PyArgumentList,PyCallByClass
            QMessageBox.critical(
                self,
                "ERREUR",
                "Problème pour enregistrer dans le fichier «{0}»:\n{1}".format(fn, e),
                buttons=QMessageBox.Close,
            )

    def get_date_range(self):
        start = self.deStart.dateTime().toPyDateTime()
        end = (
            self.deEnd.dateTime()
            .toPyDateTime()
            .replace(hour=23, minute=59, second=59, microsecond=999999)
        )
        return start, end

    def window_is_about_to_be_closed(self):
        parameters.app_set(self.PARAM_FULL_CVS, self.cbCsvFull.isChecked())
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
        self.window_is_about_to_be_closed()
        return super().accept()
