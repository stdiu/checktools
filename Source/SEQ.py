from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class SEQ(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_MO = QtWidgets.QLineEdit(Form)
        self.lineEdit_MO.setObjectName("lineEdit_MO")
        self.horizontalLayout.addWidget(self.lineEdit_MO)
        self.pushButton_MO = QtWidgets.QPushButton(Form)
        self.pushButton_MO.setObjectName("pushButton_MO")
        self.horizontalLayout.addWidget(self.pushButton_MO)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_MT = QtWidgets.QLineEdit(Form)
        self.lineEdit_MT.setObjectName("lineEdit_MT")
        self.horizontalLayout_2.addWidget(self.lineEdit_MT)
        self.pushButton_MT = QtWidgets.QPushButton(Form)
        self.pushButton_MT.setObjectName("pushButton_MT")
        self.horizontalLayout_2.addWidget(self.pushButton_MT)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_rule = QtWidgets.QLineEdit(Form)
        self.lineEdit_rule.setObjectName("lineEdit_rule")
        self.horizontalLayout_4.addWidget(self.lineEdit_rule)
        self.pushButton_rule = QtWidgets.QPushButton(Form)
        self.pushButton_rule.setObjectName("pushButton_rule")
        self.horizontalLayout_4.addWidget(self.pushButton_rule)
        self.lineEdit_dict = QtWidgets.QLineEdit(Form)
        self.lineEdit_dict.setObjectName("lineEdit_dict")
        self.horizontalLayout_4.addWidget(self.lineEdit_dict)
        self.pushButton_dict = QtWidgets.QPushButton(Form)
        self.pushButton_dict.setObjectName("pushButton_dict")
        self.horizontalLayout_4.addWidget(self.pushButton_dict)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_3.addWidget(self.progressBar)
        self.pushButton_calculate = QtWidgets.QPushButton(Form)
        self.pushButton_calculate.setObjectName("pushButton_calculate")
        self.horizontalLayout_3.addWidget(self.pushButton_calculate)
        self.pushButton_analysis = QtWidgets.QPushButton(Form)
        self.pushButton_analysis.setObjectName("pushButton_analysis")
        self.horizontalLayout_3.addWidget(self.pushButton_analysis)
        self.pushButton_abandon = QtWidgets.QPushButton(Form)
        self.pushButton_abandon.setObjectName("pushButton_abandon")
        self.horizontalLayout_3.addWidget(self.pushButton_abandon)
        self.pushButton_save = QtWidgets.QPushButton(Form)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_3.addWidget(self.pushButton_save)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab_1)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_5.addWidget(self.graphicsView)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.tab_1)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.horizontalLayout_5.addWidget(self.graphicsView_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.tab_1)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.verticalLayout_3.addWidget(self.graphicsView_4)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_MO.setText(_translate("Form", "主叫清单"))
        self.pushButton_MO.clicked.connect(self.open_MO)
        self.pushButton_MT.setText(_translate("Form", "被叫清单"))
        self.pushButton_rule.setText(_translate("Form", "筛选原则"))
        self.pushButton_dict.setText(_translate("Form", "小区台账"))
        self.pushButton_calculate.setText(_translate("Form", "统计"))
        self.pushButton_analysis.setText(_translate("Form", "智能分析"))
        self.pushButton_abandon.setText(_translate("Form", "中止"))
        self.pushButton_save.setText(_translate("Form", "导出结果"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Form", "数据可视化"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "命令提示窗"))
# ******************************************   按钮函数   **************************************************#
    def open_MO(self):      # 打开主叫清单
        self.filepath_MO, _ = QFileDialog.getOpenFileName(
            self,
            '选择主叫话单文件',
            r'./'
            '*.xlsx'
        )
        self.lineEdit_MO.setText(self.filepath_MO)

    def open_MT(self):      # 打开被叫清单
        self.filepath_MT, _ = QFileDialog.getOpenFileName(
            self,
            "选择被叫清单",
            r"./",
            '*.xlsx'
        )
        self.lineEdit_MT.setText(self.filepath_MT)

    def open_rule(self):        # 打开规则表
        self.filepath_rule, _ = QFileDialog.getOpenFileName(
            self,
            '选择筛选规则',
            r'./',
            '*.txt'
        )
        self.lineEdit_rule.setText(self.filepath_rule)

    def open_dict(self):      # 打开台账
        self.filepath_dict, _ = QFileDialog.getOpenFileName(
            self,
            '选择台账',
            r'./',
            '*.xlsx'
        )
        self.lineEdit_dict.setText(self.filepath_dict)