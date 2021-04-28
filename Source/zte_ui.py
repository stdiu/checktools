# -*- coding: UTF-8 -*-    
# Author:yansh  
# FileName:zte_ui  
# DateTime:2021/4/28 10:10  
# SoftWare: PyCharm

from PyQt5.QtWidgets import QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QStackedWidget, QGroupBox

class zte(object):
    def __init__(self):
        super(zte, self).__init__()
        self.initUI()

    def initUI(self):
        # zte总布局
        self.layout_zte = QHBoxLayout()

        # zte左布局
        zte_left = QGroupBox('参数名称')
        layout_zte_left = QVBoxLayout()
        layout_zte_left.setSpacing(1)

        btn_1 = QPushButton('4G关键参数')
        btn_2 = QPushButton('5G关键参数')
        btn_3 = QPushButton('X2')
        btn_4 = QPushButton('Xn')
        btn_5 = QPushButton('PCI')

        layout_zte_left.addWidget(btn_1)
        layout_zte_left.addWidget(btn_2)
        layout_zte_left.addWidget(btn_3)
        layout_zte_left.addWidget(btn_4)
        layout_zte_left.addWidget(btn_5)

        zte_left.setLayout(layout_zte_left)

        # zte右布局
        zte_right = QStackedWidget()

        stack1 = QWidget()
        stack2 = QWidget()
        stack3 = QWidget()
        stack4 = QWidget()
        stack5 = QWidget()


        # 添加左右布局
        self.layout_zte.addWidget(zte_left)
        self.layout_zte.addWidget(zte_right)


