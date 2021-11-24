# -*- coding: utf-8 -*-


#导入程序运行必须模块

import sys
from PyQt5.QtGui import QIcon

#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中

from PyQt5.QtWidgets import QApplication, QMainWindow

#导入designer工具生成的login模块

from login import Ui_Form

from PyQt5.QtCore import QThread, pyqtSignal,pyqtSlot

#huatu

import huatutest


class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):

        super(MyMainForm, self).__init__(parent)

        self.setupUi(self)
        self.work = WorkThread(main_win = self)
        self.work.signal.connect(self.check_ret)
        #
        self.drew.clicked.connect(self.display)
        self.exit.clicked.connect(self.close)

    def display(self):
        self.drew.setEnabled(False)
        global x, y

        x = self.x_line.text()
        y = self.y_line.text()

        self.work.start()

        self.printf('--------------------------------------\n'+'画图:' + x + '*' + y + '\n' +
                                'Start Gen Test Screen Files ...'+'\n')
        self.work.exit()

    def check_ret(self,ret):
        if ret == 1:
            self.printf('错误，请重新输入正确的分辨率')
            self.set_btn()
        else:
            self.printf('Generate Success!\n'+'保存路径：D:\pattern')
            self.set_btn()
            self.work.exit()
    
    def printf(self, mes):
        self.textBrowser.append(mes)  # 在指定的区域显示提示信息
        self.cursot = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursot.End)

    def set_btn(self):
        self.drew.setEnabled(True)

    def close(self):

        sys.exit(app.exec_())

class WorkThread(QThread):
    signal = pyqtSignal(int)

    def __init__ (self,*args,**kwargs):
        super(WorkThread, self).__init__()
        self.main_win = kwargs.get('main_win')
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