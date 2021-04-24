import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QAction, qApp, QMenu, QPushButton, QLabel, QTreeWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from HUAWEI import HUAWEI
from ZET import ZET

class test_main(QMainWindow):
    def __init__(self):
        super(test_main, self).__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('准备就绪')  # 状态栏
        self.setGeometry(300, 300, 800, 500)       # 设置起始点以及大小
        self.setWindowTitle('网优运营助手 v1.3')       # 设置项目名称
        self.setWindowIcon(QIcon(r'../Icon/中国电信.png'))
        # self.show()

        # *********************************  子菜单栏  *********************************** #
        # 文件子菜单
        exitAct = QAction(QIcon(r'../Icon./退出.png'), '退出（&E）', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出程序')
        exitAct.triggered.connect(qApp.quit)
        # 参数核查子菜单
        zetAct = QAction(QIcon(r'../Icon./中兴.png'), '中兴 (&Z)', self)
        # zetAct.setShortcut('Ctrl+Z')
        zetAct.setStatusTip('中兴参数核查')
        # zetAct.triggered.connect(ZET.Zetcheck())

        huaweiAct = QAction(QIcon(r'../Icon/华为.png'), '华为 (&W)', self)
        huaweiAct.setStatusTip('华为参数核查')
        huaweiAct.triggered.connect(lambda :HUAWEI.Huaweicheck(self))

        # *********************************  菜单栏  *********************************** #
        menubar = self.menuBar()
        # 文件
        fileMenu = menubar.addMenu('文件(&F)')
        fileMenu.addAction(exitAct)
        # 参数核查
        checkMenu = menubar.addMenu('核查(&C)')
        checkMenu.addAction(zetAct)
        checkMenu.addAction(huaweiAct)
        # 工具
        toolMenu = menubar.addMenu('工具(&T)')
        # 视图
        visualMenu = menubar.addMenu('视图(&V)')
        # 帮助
        helpMenu = menubar.addMenu('帮助(H)')
        # 文件子菜单
        saveas = QMenu('保存为(&S)', self)
        fileMenu.addMenu(saveas)

        # *********************************  设置一个中心布局  *********************************** #
        widget = QWidget()
        mianLayout = QHBoxLayout()
        self.setCentralWidget(widget)
        widget.setLayout(mianLayout)

        # 左布局
        leftlayout = QVBoxLayout()
        treewidget = QTreeWidget()
        leftlayout.addWidget(treewidget)

        # 右布局
        rightlayout = QVBoxLayout()
        # 右上布局
        rightUplayout = QVBoxLayout()
        lab1 =QLabel('标签1')
        lab2 =QLabel('标签2')
        lab3 =QLabel('标签3')
        rightUplayout.addWidget(lab1)
        rightUplayout.addWidget(lab2)
        rightUplayout.addWidget(lab3)

        # 右下布局
        rightDownlayout = QHBoxLayout()
        bt1 = QPushButton("按钮1")
        bt2 = QPushButton("按钮2")
        bt3 = QPushButton("按钮3")
        rightDownlayout.addWidget(bt1)
        rightDownlayout.addWidget(bt2)
        rightDownlayout.addWidget(bt3)


        # 右边添加布局
        rightlayout.addLayout(rightUplayout)
        rightlayout.addLayout(rightDownlayout)

        # 添加总布局
        mianLayout.addLayout(leftlayout)
        mianLayout.addLayout(rightlayout)


    # *********************************  右键菜单  *********************************** #
    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        newAct = cmenu.addAction('新建')
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == newAct:
            print('右键新建')





if __name__ == '__main__':
    app = QApplication(sys.argv)
    test_main = test_main()
    # test_main.ui.show()
    test_main.show()
    sys.exit(app.exec_())
