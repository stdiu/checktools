# -*- coding: UTF-8 -*-    
# Author:yansh  
# FileName:home_ui  
# DateTime:2021/4/26 15:08  
# SoftWare: PyCharm

from PyQt5.QtWidgets import QLabel, QVBoxLayout

class home(object):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout1 = QVBoxLayout()
        self.lab1 = QLabel(' @ 2021 中国电信广州股份有限公司  无线网络优化中心')
        self.layout1.addWidget(self.lab1)
