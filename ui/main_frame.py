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

    qss_style = """
#main_frame {
	background-color: rgb(255, 255, 255);
}

#scrollArea {
    border-style: solid;
    border-width: 1px;
	border-color: rgb(168, 168, 168);
}

#scrollAreaWidgetContents {
	background-color: rgb(244, 244, 244);
}

QPushButton {
	margin:0px 1px 1px 0px;
    border-style: solid;
    border-color: rgb(0,0,0);
    border-width: 1px;
    border-radius: 5px;
	background-color: rgb(90, 154, 250);
	color: rgb(255, 255, 255);
}
QPushButton:pressed {
	margin:1px 0px 0px 1px;
	background-color: rgb(110, 174, 255);
}
"""

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = None

        # init
        self.init()

    def init(self):
        self.ui = Ui_main_frame()
        self.ui.setupUi(self)
        self.resize(400, 300)

        self.setStyleSheet(self.qss_style)

        # 日志
        # self.signal_append_log.connect(self.ui.textEdit_log.append)


def start():
    app = QApplication(sys.argv)

    win = MainFrame()
    win.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    start()
