# -*- coding: UTF-8 -*-    
# Author:yansh  
# FileName:home_ui  
# DateTime:2021/4/26 15:08  
# SoftWare: PyCharm

import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QPushButton, QHBoxLayout, QApplication, QLabel, QTabWidget, QVBoxLayout

class home(object):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # self.mainwidget = QWidget()
        self.layout1 = QHBoxLayout()
        self.bt1 = QPushButton('这是主页面的按钮1')
        self.bt2 = QPushButton('这是主页面的按钮2')
        self.layout1.addWidget(self.bt1)
        self.layout1.addWidget(self.bt2)
        print('home主页面')

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     test_main = home()
#     sys.exit(app.exec_())
