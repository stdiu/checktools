# -*- coding: UTF-8 -*-    
# Author:yansh  
# FileName:zte_lte_key_parameters  
# DateTime:2021/5/6 15:09  
# SoftWare: PyCharm

from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox, QHBoxLayout, QLabel

class key_paraters(object):
    def __init__(self):
        super(key_paraters, self).__init__()
        self.initUI()

    def initUI(self):
        self.layout_key = QHBoxLayout()
        lab1 = QLabel('这是关键参数')
        btn_1 = QPushButton('按钮1')
        btn_1.clicked.connect(self.anniu_fuc)
        self.layout_key.addWidget(lab1)
        self.layout_key.addWidget(btn_1)

    def anniu_fuc(self):
        print('这是4G关键的按钮')