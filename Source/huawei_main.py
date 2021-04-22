import sys
import os
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon

class huawei_main(QWidget):
    def __init__(self):
        super(huawei_main, self).__init__()
        self.initUI()

    def initUI(self):
        dir = os.path.abspath('..')
        print(dir)
        self.ui = loadUi(r"{}/UI/huawei.ui".format(dir))
        # 加载lable
        self.ui.setWindowTitle("华为")
        self.ui.setWindowIcon(QIcon(r'{}/Icon/华为.png'.format(dir)))