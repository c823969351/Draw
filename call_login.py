# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_me.ui'

#

# Created by: PyQt5 UI code generator 5.11.3

#

# WARNING! All changes made in this file will be lost!

#导入程序运行必须模块

import sys
from PyQt5.QtGui import QIcon

#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中

from PyQt5.QtWidgets import QApplication, QMainWindow

#导入designer工具生成的login模块

from login import Ui_Form

from PyQt5.QtCore import QThread, pyqtSignal

#huatu

import huatutest


class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):

        super(MyMainForm, self).__init__(parent)

        self.setupUi(self)
        self.work = WorkThread()
        #

        self.drew.clicked.connect(self.display)

        self.exit.clicked.connect(self.close)

    def display(self):
        global x, y

        x = self.x_line.text()
        y = self.y_line.text()
        
        self.work.signal.connect(self.check_ret)
        self.work.start()
        
        self.textBrowser.setText('画图:' + x + '*' + y + '\n' +
                                'Start Gen Test Screen Files ...'+'\n')
    def check_ret(self,ret):
        if ret == 1:
            self.textBrowser.setText('错误，请重新输入正确的分辨率')
            self.textBrowser.repaint()
        else:
            self.textBrowser.setText('Generate Success!\n'+'保存路径：D:\pattern')

    def close(self):

        sys.exit(app.exec_())

class WorkThread(QThread):
    signal = pyqtSignal(int)

    def __init__ (self):
        super(WorkThread, self).__init__()

    def run(self):
        ret = huatutest.check_ret(x, y)
        self.signal.emit(ret)
    


if __name__ == "__main__":

    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行

    app = QApplication(sys.argv)

    #初始化

    myWin = MyMainForm()

    #将窗口控件显示在屏幕上

    myWin.show()

    #程序运行，sys.exit方法确保程序完整退出。

    sys.exit(app.exec_())