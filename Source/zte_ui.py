# -*- coding: UTF-8 -*-    
# Author:yansh  
# FileName:zte_ui  
# DateTime:2021/4/28 10:10  
# SoftWare: PyCharm

from PyQt5.QtWidgets import QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QStackedWidget, QGroupBox
from PyQt5.QtWidgets import QSpacerItem, QSizePolicy
from zte_lte_planning_parameters import test1111
from zte_lte_key_parameters import key_paraters

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

        btn_1 = QPushButton('4G规划参数')
        btn_2 = QPushButton('4G关键参数')
        btn_3 = QPushButton('VoLTE关键参数')
        btn_4 = QPushButton('负荷均衡管理')
        btn_5 = QPushButton('4G功率和功控')
        btn_6 = QPushButton('4G切换重选')
        btn_7 = QPushButton('4G频点和邻区配置')
        btn_8 = QPushButton('伪基站异常切换分析')
        btn_9 = QPushButton('4G锚点关键参数')
        btn_10 = QPushButton('锚点优选')
        btn_11 = QPushButton('邻区一致性')
        btn_12 = QPushButton('X2遗漏、冗余')
        btn_13 = QPushButton('5G关键参数')
        btn_14 = QPushButton('SA互操作参数')
        btn_15 = QPushButton('SA切换策略配置')
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        btn_1.clicked.connect(self.btn1_fuc)
        btn_2.clicked.connect(self.btn2_fuc)
        btn_3.clicked.connect(self.btn3_fuc)
        btn_4.clicked.connect(self.btn4_fuc)
        btn_5.clicked.connect(self.btn5_fuc)
        btn_6.clicked.connect(self.btn6_fuc)
        btn_7.clicked.connect(self.btn7_fuc)
        btn_8.clicked.connect(self.btn8_fuc)
        btn_9.clicked.connect(self.btn9_fuc)
        btn_10.clicked.connect(self.btn10_fuc)
        btn_11.clicked.connect(self.btn11_fuc)
        btn_12.clicked.connect(self.btn12_fuc)
        btn_13.clicked.connect(self.btn13_fuc)
        btn_14.clicked.connect(self.btn14_fuc)
        btn_15.clicked.connect(self.btn15_fuc)


        layout_zte_left.addWidget(btn_1)
        layout_zte_left.addWidget(btn_2)
        layout_zte_left.addWidget(btn_3)
        layout_zte_left.addWidget(btn_4)
        layout_zte_left.addWidget(btn_5)
        layout_zte_left.addWidget(btn_6)
        layout_zte_left.addWidget(btn_7)
        layout_zte_left.addWidget(btn_8)
        layout_zte_left.addWidget(btn_9)
        layout_zte_left.addWidget(btn_10)
        layout_zte_left.addWidget(btn_11)
        layout_zte_left.addWidget(btn_12)
        layout_zte_left.addWidget(btn_13)
        layout_zte_left.addWidget(btn_14)
        layout_zte_left.addWidget(btn_15)
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
        self.stack6 = QWidget()
        self.stack7 = QWidget()
        self.stack8 = QWidget()
        self.stack9 = QWidget()
        self.stack10 = QWidget()
        self.stack11 = QWidget()
        self.stack12 = QWidget()
        self.stack13 = QWidget()
        self.stack14 = QWidget()
        self.stack15 = QWidget()

        # 初始划控件ui
        self.stack3_ui()
        self.stack4_ui()
        self.stack5_ui()
        self.stack6_ui()
        self.stack7_ui()
        self.stack8_ui()
        self.stack9_ui()
        self.stack10_ui()
        self.stack11_ui()
        self.stack13_ui()
        self.stack14_ui()
        self.stack15_ui()

        # 添加控件
        self.zte_right.addWidget(self.stack1)
        self.zte_right.addWidget(self.stack2)
        self.zte_right.addWidget(self.stack3)
        self.zte_right.addWidget(self.stack4)
        self.zte_right.addWidget(self.stack5)
        self.zte_right.addWidget(self.stack6)
        self.zte_right.addWidget(self.stack7)
        self.zte_right.addWidget(self.stack8)
        self.zte_right.addWidget(self.stack9)
        self.zte_right.addWidget(self.stack10)
        self.zte_right.addWidget(self.stack11)
        self.zte_right.addWidget(self.stack12)
        self.zte_right.addWidget(self.stack13)
        self.zte_right.addWidget(self.stack14)
        self.zte_right.addWidget(self.stack15)

        # 添加左右布局
        self.layout_zte.addWidget(self.zte_left)
        self.layout_zte.addWidget(self.zte_right)

        # 界面引用实例化
        self.zte_lte_planning_paremeters1 = test1111()
        self.stack1.setLayout(self.zte_lte_planning_paremeters1.layout2222)

        self.lte_key_paraters = key_paraters()
        self.stack2.setLayout(self.lte_key_paraters.layout_key)

    def stack3_ui(self):
        btn1 = QPushButton('UI_3*************待开发***********************')
        layout1 = QHBoxLayout()
        layout1.addWidget(btn1)
        self.stack3.setLayout(layout1)

    def stack4_ui(self):
        btn1 = QPushButton('UI_4*************待开发***********************')
        layout1 = QHBoxLayout()
        layout1.addWidget(btn1)
        self.stack4.setLayout(layout1)

    def stack5_ui(self):
        btn1 = QPushButton('UI_5*************待开发***********************')
        layout1 = QHBoxLayout()
        layout1.addWidget(btn1)
        self.stack5.setLayout(layout1)

    def stack6_ui(self):
        btn1 = QPushButton('UI_6*************待开发***********************')
        layout1 = QHBoxLayout()
        layout1.addWidget(btn1)
        self.stack6.setLayout(layout1)

    def stack7_ui(self):
        btn1 = QPushButton('UI_7*************待开发***********************')
        layout1 = QHBoxLayout()
        layout1.addWidget(btn1)
        self.stack7.setLayout(layout1)

    def stack8_ui(self):
        btn1 = QPushButton('UI_8*************待开发***********************')
        layout1 = QHBoxLayout()
        layout1.addWidget(btn1)
        self.stack8.setLayout(layout1)

    def stack9_ui(self):
        btn1 = QPushButton('UI_9*************待开发***********************')
        layout1 = QHBoxLayout()
        layout1.addWidget(btn1)
        self.stack9.setLayout(layout1)

    def stack10_ui(self):
        btn1 = QPushButton('UI_10*************待开发***********************')
        layout1 = QHBoxLayout()
        layout1.addWidget(btn1)
        self.stack10.setLayout(layout1)

    def stack11_ui(self):
        btn1 = QPushButton('UI_11*************待开发***********************')
        layout1 = QHBoxLayout()
        layout1.addWidget(btn1)
        self.stack11.setLayout(layout1)


    def stack13_ui(self):
        btn1 = QPushButton('UI_13*************待开发***********************')
        layout1 = QHBoxLayout()
        layout1.addWidget(btn1)
        self.stack13.setLayout(layout1)

    def stack14_ui(self):
        btn1 = QPushButton('UI_14*************待开发***********************')
        layout1 = QHBoxLayout()
        layout1.addWidget(btn1)
        self.stack14.setLayout(layout1)

    def stack15_ui(self):
        btn1 = QPushButton('UI_15*************待开发***********************')
        layout1 = QHBoxLayout()
        layout1.addWidget(btn1)
        self.stack15.setLayout(layout1)

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

    def btn6_fuc(self):
        self.zte_right.setCurrentIndex(5)

    def btn7_fuc(self):
        self.zte_right.setCurrentIndex(6)

    def btn8_fuc(self):
        self.zte_right.setCurrentIndex(7)

    def btn9_fuc(self):
        self.zte_right.setCurrentIndex(8)

    def btn10_fuc(self):
        self.zte_right.setCurrentIndex(9)

    def btn11_fuc(self):
        self.zte_right.setCurrentIndex(10)

    def btn12_fuc(self):
        self.zte_right.setCurrentIndex(11)

    def btn13_fuc(self):
        self.zte_right.setCurrentIndex(12)

    def btn14_fuc(self):
        self.zte_right.setCurrentIndex(13)

    def btn15_fuc(self):
        self.zte_right.setCurrentIndex(14)







