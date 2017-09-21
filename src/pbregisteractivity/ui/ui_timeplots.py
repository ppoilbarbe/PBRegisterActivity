# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_timeplots.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TimePlots(object):
    def setupUi(self, TimePlots):
        TimePlots.setObjectName("TimePlots")
        TimePlots.resize(609, 436)
        self.layoutTimePlots = QtWidgets.QVBoxLayout(TimePlots)
        self.layoutTimePlots.setObjectName("layoutTimePlots")
        self.layoutActions = QtWidgets.QHBoxLayout()
        self.layoutActions.setObjectName("layoutActions")
        self.btnTimeSeries = QtWidgets.QToolButton(TimePlots)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons/32x32/tool_histogram.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnTimeSeries.setIcon(icon)
        self.btnTimeSeries.setObjectName("btnTimeSeries")
        self.layoutActions.addWidget(self.btnTimeSeries)
        self.btnPieChart = QtWidgets.QToolButton(TimePlots)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/icons/32x32/tool_piechart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPieChart.setIcon(icon1)
        self.btnPieChart.setObjectName("btnPieChart")
        self.layoutActions.addWidget(self.btnPieChart)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutActions.addItem(spacerItem)
        self.lblEnd = QtWidgets.QLabel(TimePlots)
        self.lblEnd.setObjectName("lblEnd")
        self.layoutActions.addWidget(self.lblEnd)
        self.deStart = QtWidgets.QDateEdit(TimePlots)
        self.deStart.setCalendarPopup(True)
        self.deStart.setObjectName("deStart")
        self.layoutActions.addWidget(self.deStart)
        self.lblEnd_2 = QtWidgets.QLabel(TimePlots)
        self.lblEnd_2.setObjectName("lblEnd_2")
        self.layoutActions.addWidget(self.lblEnd_2)
        self.deEnd = QtWidgets.QDateEdit(TimePlots)
        self.deEnd.setCalendarPopup(True)
        self.deEnd.setObjectName("deEnd")
        self.layoutActions.addWidget(self.deEnd)
        self.layoutTimePlots.addLayout(self.layoutActions)
        self.layoutPlot = QtWidgets.QVBoxLayout()
        self.layoutPlot.setObjectName("layoutPlot")
        self.layoutTimePlots.addLayout(self.layoutPlot)
        self.buttonBox = QtWidgets.QDialogButtonBox(TimePlots)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutTimePlots.addWidget(self.buttonBox)
        self.layoutTimePlots.setStretch(1, 1)

        self.retranslateUi(TimePlots)
        self.buttonBox.accepted.connect(TimePlots.accept)
        self.buttonBox.rejected.connect(TimePlots.reject)
        QtCore.QMetaObject.connectSlotsByName(TimePlots)

    def retranslateUi(self, TimePlots):
        _translate = QtCore.QCoreApplication.translate
        TimePlots.setWindowTitle(_translate("TimePlots", "Diagrammes"))
        self.lblEnd.setText(_translate("TimePlots", "Début:"))
        self.deStart.setDisplayFormat(_translate("TimePlots", "yyyy/MM/dd"))
        self.lblEnd_2.setText(_translate("TimePlots", "Fin:"))
        self.deEnd.setDisplayFormat(_translate("TimePlots", "yyyy/MM/dd"))

from . import resources_rc
