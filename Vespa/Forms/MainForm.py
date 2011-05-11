# -*- coding: utf-8 -*-

from Vespa.Forms.uiForm import Ui_Form
from PyQt4.QtGui import QWidget, QTableWidgetItem
from functools import partial
from PyQt4 import QtCore
from Vespa import Core
from PyQt4.Qwt5 import *
from PyQt4 import Qt

class Form(QWidget, Ui_Form):
        def __init__(self, parent=None):
                super(Form, self).__init__(parent)
                self.setupUi(self)
                self.spike = Core.Spike()
                calcCallback = partial(Core.calculateTheApocalypse, self, self.spike)
                self.connect(self.addOrdButton, QtCore.SIGNAL("clicked()"), self.addOrdRow)
                self.connect(self.removeOrdButton, QtCore.SIGNAL("clicked()"), self.removeOrdRow)
                self.connect(self.clearOrdButton, QtCore.SIGNAL("clicked()"), self.clearOrdTable)
                self.connect(self.addDelButton, QtCore.SIGNAL("clicked()"), self.addDelRow)
                self.connect(self.removeDelButton, QtCore.SIGNAL("clicked()"), self.removeDelRow)
                self.connect(self.clearDelButton, QtCore.SIGNAL("clicked()"), self.clearDelTable)
                self.connect(self.calcButton, QtCore.SIGNAL("clicked()"), calcCallback)
                self.ordTable.insertRow(0)
                self.ordTable.setItem(0, 0, QTableWidgetItem("1"))
                self.ordTable.setItem(0, 1, QTableWidgetItem("1.0"))
                self.delTable.insertRow(0)
                self.delTable.setItem(0, 0, QTableWidgetItem("1"))
                self.delTable.setItem(0, 1, QTableWidgetItem("1.0"))
                self.connect(self.showSizeChart, QtCore.SIGNAL("clicked()"), self.drawSizeChart)
                self.connect(self.showPeriodChart, QtCore.SIGNAL("clicked()"), self.drawPeriodChart)
                self.colors = [ Qt.Qt.blue, Qt.Qt.red, Qt.Qt.green ]

        def drawSizeChart(self):
                self.sizePlot = QwtPlot(QwtText(u"График расходов при фиксированном размере заказа"))
                self.sizePlot.insertLegend(Qwt.QwtLegend(), Qwt.QwtPlot.BottomLegend)
                for i in range(0, 3):
                        titles = [ "S = %d" % int(self.fixedSizeEdit.text()), "S = %d" % (int(self.fixedSizeEdit.text()) + 1),
                                        "S = %d" % (int(self.fixedSizeEdit.text()) - 1)]
                        try:
                                c = QwtPlotCurve(titles[i])
                                c.setData(range(1, len(self.spike.fsResults[i])), self.spike.fsResults[i])
                                c.setPen(Qt.QPen(self.colors[i]))
                                c.attach(self.sizePlot)
                        except:
                                continue
                self.sizePlot.replot()
                self.sizePlot.show()

        def drawPeriodChart(self):
                self.periodPlot = QwtPlot(QwtText(u"График расходов при фиксированном периоде заказа"))
                self.periodPlot.insertLegend(Qwt.QwtLegend(), Qwt.QwtPlot.BottomLegend)
                for i in range(0, 3):
                        titles = [ "P = %d" % int(self.fixedPeriodEdit.text()), "P = %d" % (int(self.fixedPeriodEdit.text()) + 1),
                                        "P = %d" % (int(self.fixedPeriodEdit.text()) - 1)]
                        try:    
                                c = QwtPlotCurve(titles[i])
                                c.setData(range(1, len(self.spike.fpResults[i])), self.spike.fpResults[i])
                                c.setPen(Qt.QPen(self.colors[i]))
                                c.attach(self.periodPlot)
                        except: 
                                continue
                self.periodPlot.replot()
                self.periodPlot.show()

        def addOrdRow(self):
                self.ordTable.insertRow(0)
                self.ordTable.setItem(0, 0, QTableWidgetItem(self.ordSizeEdit.text()))
                self.ordTable.setItem(0, 1, QTableWidgetItem(self.ordProbEdit.text()))

        def removeOrdRow(self):
                self.ordTable.removeRow(self.ordTable.currentRow())

        def clearOrdTable(self):
                self.ordTable.setRowCount(0)

        def addDelRow(self):
                self.delTable.insertRow(0)
                self.delTable.setItem(0, 0, QTableWidgetItem(self.delSizeEdit.text()))
                self.delTable.setItem(0, 1, QTableWidgetItem(self.delProbEdit.text()))

        def removeDelRow(self):
                self.delTable.removeRow(self.delTable.currentRow())

        def clearDelTable(self):
                self.delTable.setRowCount(0)

