# -*- coding: UTF-8 -*-    
# Author:yansh  
# FileName:zte_ui  
# DateTime:2021/4/28 10:10  
# SoftWare: PyCharm

from PyQt5.QtWidgets import QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QStackedWidget, QGroupBox,QSpacerItem, QSizePolicy

class zte(object):
    def __init__(self):
        super(zte, self).__init__()
        self.initUI()

    def initUI(self):
        # zte总布局
        self.layout_zte = QHBoxLayout()

        # zte左布局
        self.zte_left = QGroupBox('参数名称')
        layout_zte_left = QVBoxLayout()
        layout_zte_left.setSpacing(1)

        btn_1 = QPushButton('4G关键参数')
        btn_2 = QPushButton('5G关键参数')
        btn_3 = QPushButton('X2...........')
        btn_4 = QPushButton('Xn')
        btn_5 = QPushButton('PCI')
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        btn_1.clicked.connect(self.btn1_fuc)
        btn_2.clicked.connect(self.btn2_fuc)
        btn_3.clicked.connect(self.btn3_fuc)
        btn_4.clicked.connect(self.btn4_fuc)
        btn_5.clicked.connect(self.btn5_fuc)


        layout_zte_left.addWidget(btn_1)
        layout_zte_left.addWidget(btn_2)
        layout_zte_left.addWidget(btn_3)
        layout_zte_left.addWidget(btn_4)
        layout_zte_left.addWidget(btn_5)
        layout_zte_left.addItem(spacerItem)

        self.zte_left.setLayout(layout_zte_left)

        # zte右布局
        self.zte_right = QStackedWidget()

        # 创建控件
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.stack4 = QWidget()
        self.stack5 = QWidget()

        # 初始划控件ui
        self.stack1_ui()
        self.stack2_ui()
        self.stack3_ui()
        self.stack4_ui()
        self.stack5_ui()


        # 添加控件
        self.zte_right.addWidget(self.stack1)
        self.zte_right.addWidget(self.stack2)
        self.zte_right.addWidget(self.stack3)
        self.zte_right.addWidget(self.stack4)
        self.zte_right.addWidget(self.stack5)

        # 添加左右布局
        self.layout_zte.addWidget(self.zte_left)
        self.layout_zte.addWidget(self.zte_right)


    def stack1_ui(self):
        btn1 = QPushButton('UI_1')
        layout1 = QHBoxLayout()
        layout1.addWidget(btn1)
        self.stack1.setLayout(layout1)


    def stack2_ui(self):
        btn1 = QPushButton('UI_2')
        layout1 = QHBoxLayout()
        layout1.addWidget(btn1)
        self.stack2.setLayout(layout1)

    def stack3_ui(self):
        btn1 = QPushButton('UI_3')
        layout1 = QHBoxLayout()
        layout1.addWidget(btn1)
        self.stack3.setLayout(layout1)

    def stack4_ui(self):
        btn1 = QPushButton('UI_4')
        layout1 = QHBoxLayout()
        layout1.addWidget(btn1)
        self.stack4.setLayout(layout1)

    def stack5_ui(self):
        btn1 = QPushButton('UI_5')
        layout1 = QHBoxLayout()
        layout1.addWidget(btn1)
        self.stack5.setLayout(layout1)

    def btn1_fuc(self):
        self.zte_right.setCurrentIndex(0)

    def btn2_fuc(self):
        self.zte_right.setCurrentIndex(1)

    def btn3_fuc(self):
        self.zte_right.setCurrentIndex(2)

    def btn4_fuc(self):
        self.zte_right.setCurrentIndex(3)

    def btn5_fuc(self):
        self.zte_right.setCurrentIndex(4)





