import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction, qApp, QMenu
from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.uic import loadUi
from HUAWEI import HUAWEI
from ZTE import ZET

class test_main(QMainWindow):
    def __init__(self):
        super(test_main, self).__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('准备就绪')  # 状态栏
        self.setGeometry(200, 200, 1100, 700)       # 设置起始点以及大小
        self.setWindowTitle('网优运营助手 v1.3')       # 设置项目名称
        self.setWindowIcon(QIcon(r'../Icon/中国电信.png'))


        # *********************************  子菜单栏  *********************************** #
        # 文件子菜单
        backAct = QAction(QIcon(r'../Icon/主页.png'), '主页', self)
        backAct.setStatusTip('返回主页')
        backAct.triggered.connect(lambda :self.mainwidget())

        exitAct = QAction(QIcon(r'../Icon./退出.png'), '退出（&E）', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出程序')
        exitAct.triggered.connect(qApp.quit)

        # 参数核查子菜单
        zteAct = QAction(QIcon(r'../Icon./中兴.png'), '中兴 (&Z)', self)
        # zetAct.setShortcut('Ctrl+Z')
        zteAct.setStatusTip('中兴参数核查')
        zteAct.triggered.connect( lambda: ZET.Zetcheck(self))

        huaweiAct = QAction(QIcon(r'../Icon/华为.png'), '华为 (&W)', self)
        huaweiAct.setStatusTip('华为参数核查')
        huaweiAct.triggered.connect(lambda: HUAWEI.initUI(self))


        # *********************************  菜单栏  *********************************** #
        menubar = self.menuBar()
        # 文件
        fileMenu = menubar.addMenu('文件(&F)')
        fileMenu.addAction(backAct)
        fileMenu.addAction(exitAct)

        # 参数核查
        checkMenu = menubar.addMenu('核查(&C)')
        checkMenu.addAction(zteAct)
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

        # *********************************  工具栏  *********************************** #
        toolbar = self.addToolBar('工具栏')
        toolbar.addAction(backAct)
        toolbar.addAction(zteAct)
        toolbar.addAction(huaweiAct)
        toolbar.addAction(exitAct)

        self.mainwidget()  # 默认加载主页

    # *********************************  主界面  *********************************** #
    def mainwidget(self):
        mainwidget = QWidget()
        gridlayout = QGridLayout()
        pb1 = QPushButton('主界面按钮', self)
        lab1 = QLabel("主页lab", self)
        lab1.setPixmap(QPixmap(r'../Icon/中国电信.png'))
        gridlayout.addWidget(lab1)
        gridlayout.addWidget(pb1)
        mainwidget.setLayout(gridlayout)
        self.setCentralWidget(mainwidget)

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
