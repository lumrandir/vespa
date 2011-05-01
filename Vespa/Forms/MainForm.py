# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form.ui'
#
# Created: Sun May  1 10:17:25 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from Vespa.Forms.uiForm import Ui_Form
from PyQt4.QtGui import QWidget

class Form(QWidget, Ui_Form):
        def __init__(self, parent=None):
                super(Form, self).__init__(parent)
                self.setupUi(self)

