import sys
import os
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
# 加载自己写的类文件
from zhongxing_main import zhongxing_main
from huawei_main import huawei_main
from test_main import test_main

class mainWindow(QWidget):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        dir = os.path.abspath('..')
        print(dir)
        self.ui = loadUi(r"{}/UI/main.ui".format(dir))
        self.ui.pushButton_zhongxing.clicked.connect(self.jump_ZX)
        self.ui.pushButton_huawei.clicked.connect(self.jump_HW)
        self.ui.pushButton_tools.clicked.connect(self.jump_Tools)
        # 加载lable
        self.ui.setWindowTitle("分析室运营助手 v1.0")
        self.ui.setWindowIcon(QIcon(r'{}/Icon/中国电信.png'.format(dir)))

    def jump_ZX(self):
        print('跳至中兴的界面')
        self.ui.hide()
        self.jump_ZX = zhongxing_main()
        self.jump_ZX.ui.show()

    def jump_HW(self):
        print('跳至华为的界面')
        self.ui.hide()
        self.jump_HW = huawei_main()
        self.jump_HW.ui.show()

    def jump_Tools(self):
        print('跳至测试见面')
        self.ui.hide()
        self.test = test_main()
        self.test.ui.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = mainWindow()
    mainWindow.ui.show()
    sys.exit(app.exec_())
