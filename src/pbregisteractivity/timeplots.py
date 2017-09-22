#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
Dialogue utilisé pour ajouter une plage d'activité manuellement
"""

# Tested with PYTHON 3.5. Not compatible with Python 2.x

import random
import html
import csv
from io import StringIO

from datetime import date, timedelta
from PyQt5.QtWidgets import QDialog, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from .activity import activities

from .ui.ui_timeplots import Ui_TimePlots


# noinspection PyAbstractClass
class TimePlots(QDialog, Ui_TimePlots):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        today = date.today()
        self.deStart.setDate(today - timedelta(days=4))
        self.deEnd.setDate(today)

        self.deStart.dateChanged.connect(self.check_window)
        self.deEnd.dateChanged.connect(self.check_window)

        self.btnTimeSeries.clicked.connect(self.plot)
        self.btnPieChart.clicked.connect(self.handle_piechart)
        self.btnTextOutput.clicked.connect(self.handle_text_output)

        self.plot_buttons = [ self.btnTimeSeries,
                              self.btnPieChart,
                              self.btnTextOutput,
                            ]

        # a figure instance to plot on
        self._figure = Figure()

        # it takes the `figure` instance as a parameter to __init__
        self._mpl_canvas = FigureCanvas(self._figure)
        self._mpl_toolbar = NavigationToolbar(self._mpl_canvas, self)

        # set the layout
        #layout_plot = QVBoxLayout(self.frmPlot)
        self.layoutPlot.addWidget(self._mpl_canvas)
        self.layoutPlot.addWidget(self._mpl_toolbar)
        #self.frmPlot.setLayout(layout_plot)
        self.set_text(None)

    def check_window(self):
        for x in self.plot_buttons:
            if x.isChecked():
                x.click()
                break

    def plot(self):
        """ plot some random stuff """
        self.set_text(False)
        # random data
        data = [random.random() for i in range(10)]

        # create an axis
        ax = self._figure.add_subplot(111)

        # discards the old graph
        ax.clear()

        # plot data
        ax.plot(data, '*-')

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

        ax = self._figure.add_subplot(111)
        ax.clear()
        ax.pie(values, labels=labels, autopct='%1.1f%%')
        # Ratio d'aspect égal entre x et y ==> cercle
        ax.axis('equal')
        # Rafraichis le canevas
        self._mpl_canvas.draw()

    def handle_text_output(self):
        self.set_text(True)
        start, end = self.get_date_range()
        what = activities.pack_durations(start=start, end=end)
        txt = ""
        strio = StringIO(newline='')
        csvio = csv.DictWriter(strio,
                               quoting=csv.QUOTE_ALL,
                               fieldnames=["nom", "durée", "commentaires"])
        csvio.writeheader()
        for k, v in what.items():
            txt += "<h1>{0}</h1>".format(html.escape(k))
            txt += "Durée: {:1.2f}h<br>".format(v['duration']/3600.0)
            if len(v['comments']) > 0:
                txt += "<ul>"
                for x in v['comments']:
                    txt += "<li>{}</li>".format(html.escape(x))
                txt += "</ul>"
            csvio.writerow(dict(
                nom=k,
                durée="{:1.2f}".format(v['duration']/3600.0),
                commentaires="\n".join(v['comments']),
            ))
        self.edtHtml.setHtml(txt)
        self.edtCsv.setPlainText(strio.getvalue())


    def set_text(self, text):
        self.frmTextOutput.setVisible(text is not None and text)
        self.frmPlot.setVisible(text is not None and not text)

    def get_date_range(self):
        start = self.deStart.dateTime().toPyDateTime()
        end = self.deEnd.dateTime().toPyDateTime().replace(hour=23, minute=59, second=59, microsecond=999999)
        return start, end
