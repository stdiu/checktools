import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction, qApp, QMenu, QStackedWidget
from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.uic import loadUi
from HUAWEI import HUAWEI
from ZTE import ZET
from SEQ import SEQ
from home_ui import home


class SEQ_UI(QWidget, SEQ):
    def __init__(self):
        super(SEQ_UI, self).__init__()
        self.setupUi(self)
        print('SEQ实例化')

# class home_UI(QWidget, home):
#     def __init__(self):
#         super(home_UI, self).__init__()
#         print('home实例化')

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
        backAct.setObjectName('backAct')
        backAct.triggered.connect(self.switch)

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

        # 工具子菜单栏
        seqAct = QAction(QIcon(r'../Icon/SEQ.png'),'SEQ话单分析', self)
        seqAct.setText('SEQ话单统计')
        seqAct.setObjectName('seqAct')
        seqAct.triggered.connect(self.switch)


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
        toolMenu.addAction(seqAct)
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
        toolbar.addAction(seqAct)
        toolbar.addAction(exitAct)

        # 实例化一个QStackedWidget
        self.mainwidget = QStackedWidget()
        self.setCentralWidget(self.mainwidget)

        # 实例化分页面
        self.home = home()
        self.SEQ = SEQ_UI()

        # 将界面加入布局中
        self.mainwidget.addWidget(self.SEQ)
        self.mainwidget.addWidget(self.home)


    # *********************************  右键菜单  *********************************** #
    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        newAct = cmenu.addAction('新建')
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == newAct:
            print('右键新建')

    # *********************************  点击轮询函数  *********************************** #
    def switch(self):
        sender = self.sender().objectName()
        print(sender)

        index = {
            "seqAct": 0,
            "backAct": 1,
            "huaweiAct": 2
        }
        print('索引：', index[sender])
        self.mainwidget.setCurrentIndex(index[sender])




if __name__ == '__main__':
    app = QApplication(sys.argv)
    test_main = test_main()
    # test_main.ui.show()
    test_main.show()
    sys.exit(app.exec_())
