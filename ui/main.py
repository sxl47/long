#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: sxl
@file: main.py
@time: 2018/9/18 21:19:55
@desc:

"""
import sys
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QWidget, QApplication

from ui.main_frame_ui import Ui_main_frame


class MainFrame(QWidget):
    signal_append_log = pyqtSignal(str)

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = None

        # init
        self.init()

    def init(self):
        self.ui = Ui_main_frame()
        self.ui.setupUi(self)
        self.resize(1024, 750)

        # 日志
        # self.signal_append_log.connect(self.ui.textEdit_log.append)


def start():
    app = QApplication(sys.argv)

    win = MainFrame()
    win.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    start()
