from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton
import os
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QTabWidget
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon

class HUAWEI(QWidget):

    def initUI(self):
        self.btn_1 = QPushButton('1', self)
        self.btn_2 = QPushButton('2', self)
        self.btn_3 = QPushButton('3', self)
        self.btn_4 = QPushButton('4', self)

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.btn_1)
        left_layout.addWidget(self.btn_2)
        left_layout.addWidget(self.btn_3)
        left_layout.addWidget(self.btn_4)
        left_layout.addStretch(5)
        left_layout.setSpacing(20)
        left_widget = QWidget()
        left_widget.setLayout(left_layout)

        self.right_widget = QTabWidget()
        self.right_widget.tabBar().setObjectName("mainTab")

        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(self.right_widget)
        main_layout.setStretch(0, 40)
        main_layout.setStretch(1, 200)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.btn_1.clicked.connect(lambda: HUAWEI.Test(self))
    def Test(self):
        print('打印输出测试')


