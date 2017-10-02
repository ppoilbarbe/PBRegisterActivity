#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
Dialogue utilisé pour ajouter une plage d'activité manuellement
"""

# Tested with PYTHON 3.5. Not compatible with Python 2.x

import csv
import html
import re
from datetime import date, timedelta
from io import StringIO

from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.dates import DateFormatter, DayLocator, HourLocator
from matplotlib.figure import Figure

from .activity import activities
from .ui.ui_timeplots import Ui_TimePlots


# noinspection PyAbstractClass
class TimePlots(QDialog, Ui_TimePlots):

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

        self.btnToday.clicked.connect(self.handle_today)
        self.btnWorkWeek.clicked.connect(self.handle_workweek)

        self.btnHtmlSave.clicked.connect(self.handle_savehtml)
        self.btnCsvSave.clicked.connect(self.handle_savecsv)

        self.plot_buttons = [ self.btnTimeLines,
                              self.btnPieChart,
                              self.btnTextOutput,
                            ]

        self._figure = Figure()

        self._mpl_canvas = FigureCanvas(self._figure)
        self._mpl_toolbar = NavigationToolbar(self._mpl_canvas, self)

        self.layoutPlot.addWidget(self._mpl_canvas)
        self.layoutPlot.addWidget(self._mpl_toolbar)
        self.set_text(None)

    def check_window(self):
        for x in self.plot_buttons:
            if x.isChecked():
                x.click()
                break

    def handle_today(self):
        today = date.today()
        self.deStart.setDate(today)
        self.deEnd.setDate(today)
        self.check_window()

    def handle_workweek(self):
        today = date.today()
        self.deStart.setDate(today - timedelta(days=today.weekday()))
        self.deEnd.setDate(today)
        self.check_window()

    def handle_timelines(self):
        self.set_text(False)
        start, end = self.get_date_range()
        what = activities.pack_by_name(start=start, end=end)
        plt = self._figure.add_subplot(111)
        plt.clear()

        if len(what) > 0:
            plt.xaxis.set_major_locator(DayLocator())
            plt.xaxis.set_major_formatter(DateFormatter('%b-%d'))
            plt.xaxis.set_minor_locator(HourLocator(interval=2))
            ylabels = []
            y = []
            datemin = None
            datemax = None
            for k,v in what.items():
                ylabels.append(k)
                y.append(len(ylabels))
                x1 = [ x.start for x in v ]
                x2 = [ x.end for x in v ]
                tmp = min(x1)
                if datemin is None or tmp < datemin:
                    datemin = tmp
                tmp = max(x1)
                if datemax is None or tmp > datemax:
                    datemax = tmp
                print(y[-1])
                print(x1)
                print(x2)
                plt.hlines([y[-1]] * len(x1), x1, x2, lw=2, color='red')
            plt.set_ylim(len(ylabels) + 0.5, 0.5)
            plt.set_yticks(y)
            plt.set_yticklabels(ylabels)
            datemin -= timedelta(hours=4.0)
            datemax += timedelta(hours=4.0)
            plt.xaxis_date()
            for x in plt.xaxis.get_ticklabels():
                x.set_rotation(45)
                x.set_horizontalalignment('right')
            plt.set_xlim(left=datemin, right=datemax)
#            plt.xaxis.set_data_interval(datemin, datemax)

        # refresh canvas
        self._mpl_canvas.draw()

    def handle_piechart(self):
        self.set_text(False)
        start, end = self.get_date_range()
        what = activities.pack_durations(start=start, end=end)
        labels = []
        values = []
        miscelaneous = 0.0
        for k, v in what.items():
            d = v['duration']
            if d < 3600.0:
                miscelaneous += d
            else:
                labels.append("{} - {:1.2f}h".format(k, d/3600.0))
                values.append(d)
        if miscelaneous > 0:
            labels.append("Divers - {:1.2f}h".format(miscelaneous / 3600.0))
            values.append(miscelaneous)

        plt = self._figure.add_subplot(111)
        plt.clear()
        plt.pie(values, labels=labels, autopct='%1.1f%%')
        # Ratio d'aspect égal entre x et y ==> cercle
        plt.axis('equal')
        # Rafraichis le canevas
        self._mpl_canvas.draw()

    def handle_text_output(self):
        self.set_text(True)
        start, end = self.get_date_range()
        what = activities.pack_durations(start=start, end=end)
        txt = ""
        strio = StringIO(newline='')
        partial = not self.cbCsvFull.isChecked()
        if partial:
            csvio = csv.DictWriter(strio,
                                   quoting=csv.QUOTE_ALL,
                                   fieldnames=["nom", "duree", "commentaires"])
        else:
            csvio = csv.DictWriter(strio,
                                   quoting=csv.QUOTE_ALL,
                                   fieldnames=["nom", "debut", "fin", "duree", "duree_heures", "commentaires"])
        csvio.writeheader()
        for k, v in what.items():
            txt += "<h1>{0}</h1>".format(html.escape(k))
            txt += "Durée: {:1.2f}h<br>".format(v['duration']/3600.0)
            if len(v['comments']) > 0:
                txt += "<ul>"
                for x in v['comments']:
                    lines = [ html.escape(l) for l in re.split("[\r\n]+", x) if l != "" ]
                    txt += "<li>{}</li>".format("<br>".join(lines))
                txt += "</ul>"
            if partial:
                csvio.writerow(dict(
                    nom=k,
                    duree="{:1.2f}".format(v['duration']/3600.0),
                    commentaires="\n".join(v['comments']),
                ))
        if not partial:
            for k,v in activities.pack_by_name(start=start, end=end).items():
                for activity in v:
                    delta = activity.end-activity.start

                    csvio.writerow(dict(
                        nom=k,
                        debut=activity.start.strftime("%Y-%m-%d %H:%M:%S"),
                        fin=activity.end.strftime("%Y-%m-%d %H:%M:%S"),
                        duree="{}".format(delta),
                        duree_heures="{:1.3f}".format(delta.total_seconds()/3600.0),
                        commentaires=activity.comment))

        self.edtHtml.setHtml(txt+"\n")
        self.edtCsv.setPlainText(strio.getvalue())

    def handle_savehtml(self):
        self.save_text(kind="HTML", ext=".html", text=self.edtHtml.toHtml())

    def handle_savecsv(self):
        self.save_text(kind="CSV", ext=".csv", text=self.edtCsv.toPlainText())

    def set_text(self, text):
        self.frmTextOutput.setVisible(text is not None and text)
        self.frmPlot.setVisible(text is not None and not text)

    def save_text(self, kind="Text", ext=".txt", text=""):
        if text is None or len(text) == 0:
            return
        filter = "{0} (*{1});; Texte (*.txt);; Tous les fichiers (*)".format(kind, ext)
        fn,flt = QFileDialog.getSaveFileName(self,
                                           caption="Sauvegarde au format {0}".format(kind),
                                           filter=filter,
                                           options=QFileDialog.DontResolveSymlinks)
        if fn is None or fn == "":
            return
        try:
            with open(fn, "w") as f:
                f.write(text)
            QMessageBox.information(self,
                                    "SAUVEGARDE",
                                    "Fichier {} «{}» créé.".format(kind, fn),
                                    buttons=QMessageBox.Ok)
        except IOError as e:
            QMessageBox.critical(self,
                                 "ERREUR",
                                 "Problème pour enregistrer dans le fichier «{0}»:\n{1}".format(
                                     fn,
                                     e,
                                 ),
                                 buttons=QMessageBox.Close)



    def get_date_range(self):
        start = self.deStart.dateTime().toPyDateTime()
        end = self.deEnd.dateTime().toPyDateTime().replace(hour=23, minute=59, second=59, microsecond=999999)
        return start, end
