# -*- coding: utf-8 -*-

from Vespa.Forms.uiForm import Ui_Form
from PyQt4.QtGui import QWidget, QTableWidgetItem
from functools import partial
from PyQt4 import QtCore
from Vespa import Core

class Form(QWidget, Ui_Form):
        def __init__(self, parent=None):
                super(Form, self).__init__(parent)
                self.setupUi(self)

                calcCallback = partial(Core.calculateTheApocalypse, self)
                self.connect(self.addOrdButton, QtCore.SIGNAL("clicked()"), self.addOrdRow)
                self.connect(self.removeOrdButton, QtCore.SIGNAL("clicked()"), self.removeOrdRow)
                self.connect(self.clearOrdButton, QtCore.SIGNAL("clicked()"), self.clearOrdTable)
                self.connect(self.addDelButton, QtCore.SIGNAL("clicked()"), self.addDelRow)
                self.connect(self.removeDelButton, QtCore.SIGNAL("clicked()"), self.removeDelRow)
                self.connect(self.clearDelButton, QtCore.SIGNAL("clicked()"), self.clearDelTable)
                self.connect(self.calcButton, QtCore.SIGNAL("clicked()"), calcCallback)

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

