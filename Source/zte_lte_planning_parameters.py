# -*- coding: UTF-8 -*-    
# Author:yansh  
# FileName:zte_lte_planning_parameters  
# DateTime:2021/5/6 9:42  
# SoftWare: PyCharm

from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox, QHBoxLayout, QLabel

class test1111(object):
    def __init__(self):
        super(test1111, self).__init__()
        self.initUI()

    def initUI(self):
        self.layout2222 = QHBoxLayout()
        self.lab1 = QLabel('这是g规划类参数')
        btn_1 = QPushButton('按钮1')
        btn_1.clicked.connect(self.anniu_fuc)
        self.layout2222.addWidget(self.lab1)
        self.layout2222.addWidget(btn_1)

    def anniu_fuc(self):
        print('这是4G规划参数的按钮')




