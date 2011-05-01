#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
import sys
from Vespa.Forms.MainForm import Form

if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  window = Form()
  window.show()
  sys.exit(app.exec_())

