# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form.ui'
#
# Created: Sun May  1 10:25:15 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(841, 446)
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 224, 332))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.initialStorageLabel = QtGui.QLabel(self.layoutWidget)
        self.initialStorageLabel.setObjectName("initialStorageLabel")
        self.verticalLayout.addWidget(self.initialStorageLabel)
        self.initialStorageEdit = QtGui.QLineEdit(self.layoutWidget)
        self.initialStorageEdit.setObjectName("initialStorageEdit")
        self.verticalLayout.addWidget(self.initialStorageEdit)
        self.countPeriodLabel = QtGui.QLabel(self.layoutWidget)
        self.countPeriodLabel.setObjectName("countPeriodLabel")
        self.verticalLayout.addWidget(self.countPeriodLabel)
        self.countPeriodEdit = QtGui.QLineEdit(self.layoutWidget)
        self.countPeriodEdit.setObjectName("countPeriodEdit")
        self.verticalLayout.addWidget(self.countPeriodEdit)
        self.fixedPeriodLabel = QtGui.QLabel(self.layoutWidget)
        self.fixedPeriodLabel.setObjectName("fixedPeriodLabel")
        self.verticalLayout.addWidget(self.fixedPeriodLabel)
        self.fixedPeriodEdit = QtGui.QLineEdit(self.layoutWidget)
        self.fixedPeriodEdit.setObjectName("fixedPeriodEdit")
        self.verticalLayout.addWidget(self.fixedPeriodEdit)
        self.fixedSizeLabel = QtGui.QLabel(self.layoutWidget)
        self.fixedSizeLabel.setObjectName("fixedSizeLabel")
        self.verticalLayout.addWidget(self.fixedSizeLabel)
        self.fixedSizeEdit = QtGui.QLineEdit(self.layoutWidget)
        self.fixedSizeEdit.setObjectName("fixedSizeEdit")
        self.verticalLayout.addWidget(self.fixedSizeEdit)
        self.maxPeriodLabel = QtGui.QLabel(self.layoutWidget)
        self.maxPeriodLabel.setObjectName("maxPeriodLabel")
        self.verticalLayout.addWidget(self.maxPeriodLabel)
        self.maxPeriodEdit = QtGui.QLineEdit(self.layoutWidget)
        self.maxPeriodEdit.setObjectName("maxPeriodEdit")
        self.verticalLayout.addWidget(self.maxPeriodEdit)
        self.maxSizeLabel = QtGui.QLabel(self.layoutWidget)
        self.maxSizeLabel.setObjectName("maxSizeLabel")
        self.verticalLayout.addWidget(self.maxSizeLabel)
        self.maxSizeEdit = QtGui.QLineEdit(self.layoutWidget)
        self.maxSizeEdit.setObjectName("maxSizeEdit")
        self.verticalLayout.addWidget(self.maxSizeEdit)
        self.layoutWidget1 = QtGui.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(240, 10, 351, 209))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ordSizeLabel = QtGui.QLabel(self.layoutWidget1)
        self.ordSizeLabel.setObjectName("ordSizeLabel")
        self.verticalLayout_3.addWidget(self.ordSizeLabel)
        self.ordSizeEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.ordSizeEdit.setObjectName("ordSizeEdit")
        self.verticalLayout_3.addWidget(self.ordSizeEdit)
        self.ordProbLabel = QtGui.QLabel(self.layoutWidget1)
        self.ordProbLabel.setObjectName("ordProbLabel")
        self.verticalLayout_3.addWidget(self.ordProbLabel)
        self.ordProbEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.ordProbEdit.setObjectName("ordProbEdit")
        self.verticalLayout_3.addWidget(self.ordProbEdit)
        self.addOrdButton = QtGui.QPushButton(self.layoutWidget1)
        self.addOrdButton.setObjectName("addOrdButton")
        self.verticalLayout_3.addWidget(self.addOrdButton)
        self.removeOrdButton = QtGui.QPushButton(self.layoutWidget1)
        self.removeOrdButton.setObjectName("removeOrdButton")
        self.verticalLayout_3.addWidget(self.removeOrdButton)
        self.clearOrdButton = QtGui.QPushButton(self.layoutWidget1)
        self.clearOrdButton.setObjectName("clearOrdButton")
        self.verticalLayout_3.addWidget(self.clearOrdButton)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.ordTable = QtGui.QTableWidget(self.layoutWidget1)
        self.ordTable.setObjectName("ordTable")
        self.ordTable.setColumnCount(2)
        self.ordTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.ordTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.ordTable.setHorizontalHeaderItem(1, item)
        self.horizontalLayout.addWidget(self.ordTable)
        self.layoutWidget_2 = QtGui.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(240, 230, 351, 209))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.delSizeLabel = QtGui.QLabel(self.layoutWidget_2)
        self.delSizeLabel.setObjectName("delSizeLabel")
        self.verticalLayout_4.addWidget(self.delSizeLabel)
        self.delSizeEdit = QtGui.QLineEdit(self.layoutWidget_2)
        self.delSizeEdit.setObjectName("delSizeEdit")
        self.verticalLayout_4.addWidget(self.delSizeEdit)
        self.delProbLabel = QtGui.QLabel(self.layoutWidget_2)
        self.delProbLabel.setObjectName("delProbLabel")
        self.verticalLayout_4.addWidget(self.delProbLabel)
        self.delProbEdit = QtGui.QLineEdit(self.layoutWidget_2)
        self.delProbEdit.setObjectName("delProbEdit")
        self.verticalLayout_4.addWidget(self.delProbEdit)
        self.addDelButton = QtGui.QPushButton(self.layoutWidget_2)
        self.addDelButton.setObjectName("addDelButton")
        self.verticalLayout_4.addWidget(self.addDelButton)
        self.removeDelButton = QtGui.QPushButton(self.layoutWidget_2)
        self.removeDelButton.setObjectName("removeDelButton")
        self.verticalLayout_4.addWidget(self.removeDelButton)
        self.clearDelButton = QtGui.QPushButton(self.layoutWidget_2)
        self.clearDelButton.setObjectName("clearDelButton")
        self.verticalLayout_4.addWidget(self.clearDelButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.delTable = QtGui.QTableWidget(self.layoutWidget_2)
        self.delTable.setObjectName("delTable")
        self.delTable.setColumnCount(2)
        self.delTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.delTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.delTable.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_2.addWidget(self.delTable)
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(607, 10, 226, 383))
        self.widget.setObjectName("widget")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.unitCostLabel = QtGui.QLabel(self.widget)
        self.unitCostLabel.setObjectName("unitCostLabel")
        self.verticalLayout_2.addWidget(self.unitCostLabel)
        self.unitCostEdit = QtGui.QLineEdit(self.widget)
        self.unitCostEdit.setObjectName("unitCostEdit")
        self.verticalLayout_2.addWidget(self.unitCostEdit)
        self.orderCostLabel = QtGui.QLabel(self.widget)
        self.orderCostLabel.setObjectName("orderCostLabel")
        self.verticalLayout_2.addWidget(self.orderCostLabel)
        self.orderCostEdit = QtGui.QLineEdit(self.widget)
        self.orderCostEdit.setObjectName("orderCostEdit")
        self.verticalLayout_2.addWidget(self.orderCostEdit)
        self.deficitCostLabel = QtGui.QLabel(self.widget)
        self.deficitCostLabel.setObjectName("deficitCostLabel")
        self.verticalLayout_2.addWidget(self.deficitCostLabel)
        self.deficitCostEdit = QtGui.QLineEdit(self.widget)
        self.deficitCostEdit.setObjectName("deficitCostEdit")
        self.verticalLayout_2.addWidget(self.deficitCostEdit)
        self.verticalLayout_7.addLayout(self.verticalLayout_2)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.resultPeriodLabel = QtGui.QLabel(self.widget)
        self.resultPeriodLabel.setObjectName("resultPeriodLabel")
        self.verticalLayout_5.addWidget(self.resultPeriodLabel)
        self.resultPeriodEdit = QtGui.QLineEdit(self.widget)
        self.resultPeriodEdit.setObjectName("resultPeriodEdit")
        self.verticalLayout_5.addWidget(self.resultPeriodEdit)
        self.showPeriodChart = QtGui.QPushButton(self.widget)
        self.showPeriodChart.setObjectName("showPeriodChart")
        self.verticalLayout_5.addWidget(self.showPeriodChart)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.resultSizeLabel = QtGui.QLabel(self.widget)
        self.resultSizeLabel.setObjectName("resultSizeLabel")
        self.verticalLayout_6.addWidget(self.resultSizeLabel)
        self.resultSizeEdit = QtGui.QLineEdit(self.widget)
        self.resultSizeEdit.setObjectName("resultSizeEdit")
        self.verticalLayout_6.addWidget(self.resultSizeEdit)
        self.showSizeChart = QtGui.QPushButton(self.widget)
        self.showSizeChart.setObjectName("showSizeChart")
        self.verticalLayout_6.addWidget(self.showSizeChart)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.calcButton = QtGui.QPushButton(self.widget)
        self.calcButton.setObjectName("calcButton")
        self.horizontalLayout_3.addWidget(self.calcButton)
        self.quitButton = QtGui.QPushButton(self.widget)
        self.quitButton.setObjectName("quitButton")
        self.horizontalLayout_3.addWidget(self.quitButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.quitButton, QtCore.SIGNAL("clicked()"), Form.close)
        QtCore.QObject.connect(self.clearDelButton, QtCore.SIGNAL("clicked()"), self.delTable.clearContents)
        QtCore.QObject.connect(self.clearOrdButton, QtCore.SIGNAL("clicked()"), self.ordTable.clearContents)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "gVespa", None, QtGui.QApplication.UnicodeUTF8))
        self.initialStorageLabel.setText(QtGui.QApplication.translate("Form", "Стартовый запас", None, QtGui.QApplication.UnicodeUTF8))
        self.initialStorageEdit.setInputMask(QtGui.QApplication.translate("Form", "00000; ", None, QtGui.QApplication.UnicodeUTF8))
        self.initialStorageEdit.setText(QtGui.QApplication.translate("Form", "100", None, QtGui.QApplication.UnicodeUTF8))
        self.countPeriodLabel.setText(QtGui.QApplication.translate("Form", "Период расчёта", None, QtGui.QApplication.UnicodeUTF8))
        self.countPeriodEdit.setInputMask(QtGui.QApplication.translate("Form", "0000; ", None, QtGui.QApplication.UnicodeUTF8))
        self.countPeriodEdit.setText(QtGui.QApplication.translate("Form", "365", None, QtGui.QApplication.UnicodeUTF8))
        self.fixedPeriodLabel.setText(QtGui.QApplication.translate("Form", "Фиксированный период", None, QtGui.QApplication.UnicodeUTF8))
        self.fixedPeriodEdit.setInputMask(QtGui.QApplication.translate("Form", "000; ", None, QtGui.QApplication.UnicodeUTF8))
        self.fixedPeriodEdit.setText(QtGui.QApplication.translate("Form", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.fixedSizeLabel.setText(QtGui.QApplication.translate("Form", "Фиксированный размер заказа", None, QtGui.QApplication.UnicodeUTF8))
        self.fixedSizeEdit.setInputMask(QtGui.QApplication.translate("Form", "000; ", None, QtGui.QApplication.UnicodeUTF8))
        self.fixedSizeEdit.setText(QtGui.QApplication.translate("Form", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.maxPeriodLabel.setText(QtGui.QApplication.translate("Form", "Максимальный период", None, QtGui.QApplication.UnicodeUTF8))
        self.maxPeriodEdit.setInputMask(QtGui.QApplication.translate("Form", "000; ", None, QtGui.QApplication.UnicodeUTF8))
        self.maxPeriodEdit.setText(QtGui.QApplication.translate("Form", "20", None, QtGui.QApplication.UnicodeUTF8))
        self.maxSizeLabel.setText(QtGui.QApplication.translate("Form", "Максимальный размер заказа", None, QtGui.QApplication.UnicodeUTF8))
        self.maxSizeEdit.setInputMask(QtGui.QApplication.translate("Form", "000; ", None, QtGui.QApplication.UnicodeUTF8))
        self.maxSizeEdit.setText(QtGui.QApplication.translate("Form", "20", None, QtGui.QApplication.UnicodeUTF8))
        self.ordSizeLabel.setText(QtGui.QApplication.translate("Form", "Величина спроса", None, QtGui.QApplication.UnicodeUTF8))
        self.ordSizeEdit.setInputMask(QtGui.QApplication.translate("Form", "000; ", None, QtGui.QApplication.UnicodeUTF8))
        self.ordSizeEdit.setText(QtGui.QApplication.translate("Form", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.ordProbLabel.setText(QtGui.QApplication.translate("Form", "Вес величины", None, QtGui.QApplication.UnicodeUTF8))
        self.ordProbEdit.setInputMask(QtGui.QApplication.translate("Form", "0.00; ", None, QtGui.QApplication.UnicodeUTF8))
        self.ordProbEdit.setText(QtGui.QApplication.translate("Form", "1.00", None, QtGui.QApplication.UnicodeUTF8))
        self.addOrdButton.setText(QtGui.QApplication.translate("Form", "Добавить", None, QtGui.QApplication.UnicodeUTF8))
        self.removeOrdButton.setText(QtGui.QApplication.translate("Form", "Удалить", None, QtGui.QApplication.UnicodeUTF8))
        self.clearOrdButton.setText(QtGui.QApplication.translate("Form", "Очистить", None, QtGui.QApplication.UnicodeUTF8))
        self.ordTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Form", "Значение", None, QtGui.QApplication.UnicodeUTF8))
        self.ordTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Form", "Вес", None, QtGui.QApplication.UnicodeUTF8))
        self.delSizeLabel.setText(QtGui.QApplication.translate("Form", "Срок поставки", None, QtGui.QApplication.UnicodeUTF8))
        self.delSizeEdit.setInputMask(QtGui.QApplication.translate("Form", "00; ", None, QtGui.QApplication.UnicodeUTF8))
        self.delSizeEdit.setText(QtGui.QApplication.translate("Form", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.delProbLabel.setText(QtGui.QApplication.translate("Form", "Вес величины", None, QtGui.QApplication.UnicodeUTF8))
        self.delProbEdit.setInputMask(QtGui.QApplication.translate("Form", "0.00; ", None, QtGui.QApplication.UnicodeUTF8))
        self.delProbEdit.setText(QtGui.QApplication.translate("Form", "1.00", None, QtGui.QApplication.UnicodeUTF8))
        self.addDelButton.setText(QtGui.QApplication.translate("Form", "Добавить", None, QtGui.QApplication.UnicodeUTF8))
        self.removeDelButton.setText(QtGui.QApplication.translate("Form", "Удалить", None, QtGui.QApplication.UnicodeUTF8))
        self.clearDelButton.setText(QtGui.QApplication.translate("Form", "Очистить", None, QtGui.QApplication.UnicodeUTF8))
        self.delTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Form", "Размер", None, QtGui.QApplication.UnicodeUTF8))
        self.delTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Form", "Вес", None, QtGui.QApplication.UnicodeUTF8))
        self.unitCostLabel.setText(QtGui.QApplication.translate("Form", "Затраты на хранение единицы", None, QtGui.QApplication.UnicodeUTF8))
        self.unitCostEdit.setInputMask(QtGui.QApplication.translate("Form", "00; ", None, QtGui.QApplication.UnicodeUTF8))
        self.unitCostEdit.setText(QtGui.QApplication.translate("Form", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.orderCostLabel.setText(QtGui.QApplication.translate("Form", "Затраты на оформление заказа", None, QtGui.QApplication.UnicodeUTF8))
        self.orderCostEdit.setInputMask(QtGui.QApplication.translate("Form", "00; ", None, QtGui.QApplication.UnicodeUTF8))
        self.orderCostEdit.setText(QtGui.QApplication.translate("Form", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.deficitCostLabel.setText(QtGui.QApplication.translate("Form", "Штраф за дефицит единицы", None, QtGui.QApplication.UnicodeUTF8))
        self.deficitCostEdit.setInputMask(QtGui.QApplication.translate("Form", "00; ", None, QtGui.QApplication.UnicodeUTF8))
        self.deficitCostEdit.setText(QtGui.QApplication.translate("Form", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.resultPeriodLabel.setText(QtGui.QApplication.translate("Form", "Оптимальный период заказов", None, QtGui.QApplication.UnicodeUTF8))
        self.showPeriodChart.setText(QtGui.QApplication.translate("Form", "Показать график", None, QtGui.QApplication.UnicodeUTF8))
        self.resultSizeLabel.setText(QtGui.QApplication.translate("Form", "Оптимальный размер заказа", None, QtGui.QApplication.UnicodeUTF8))
        self.showSizeChart.setText(QtGui.QApplication.translate("Form", "Показать график", None, QtGui.QApplication.UnicodeUTF8))
        self.calcButton.setText(QtGui.QApplication.translate("Form", "Расчёт", None, QtGui.QApplication.UnicodeUTF8))
        self.quitButton.setText(QtGui.QApplication.translate("Form", "Выход", None, QtGui.QApplication.UnicodeUTF8))

