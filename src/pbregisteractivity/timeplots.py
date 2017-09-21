#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
Dialogue utilisé pour ajouter une plage d'activité manuellement
"""

# Tested with PYTHON 3.5. Not compatible with Python 2.x

from PyQt5.QtWidgets import QDialog, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import random
from .ui.ui_timeplots import Ui_TimePlots


# noinspection PyAbstractClass
class TimePlots(QDialog, Ui_TimePlots):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # a figure instance to plot on
        self._figure = Figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self._mpl_canvas = FigureCanvas(self._figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self._mpl_toolbar = NavigationToolbar(self._mpl_canvas, self)

        # Just some button connected to `plot` method
        self.btnTimeSeries.clicked.connect(self.plot)

        # set the layout
        self.layoutPlot.addWidget(self._mpl_canvas)
        self.layoutPlot.addWidget(self._mpl_toolbar)

    def plot(self):
        ''' plot some random stuff '''
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
