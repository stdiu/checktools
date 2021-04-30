import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction, qApp, QMenu, QStackedWidget
from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.uic import loadUi
from ZTE import ZET
from SEQ import SEQ
from home_ui import home
from zte_ui import zte
from huawei_ui import huawei


class SEQ_UI(QWidget, SEQ):
    def __init__(self):
        super(SEQ_UI, self).__init__()
        self.setupUi(self)
        print('SEQ实例化')

class HUAWEI_UI(QWidget, huawei):
    def __init__(self):
        super(HUAWEI_UI, self).__init__()
        self.setupUi(self)
        print("huawei实例化")

class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('准备就绪')  # 状态栏
        self.setGeometry(200, 200, 1100, 700)       # 设置起始点以及大小
        self.setWindowTitle('网优运营助手 v1.3')       # 设置项目名称
        self.setWindowIcon(QIcon(r'../Icon/中国电信.png'))


        # *********************************  子菜单栏  *********************************** #
        # 文件子菜单
        homeAct = QAction(QIcon(r'../Icon/主页.png'), '主页', self)
        homeAct.setStatusTip('返回主页')
        homeAct.setObjectName('homeAct')
        homeAct.triggered.connect(self.switch)

        exitAct = QAction(QIcon(r'../Icon./退出.png'), '退出（&E）', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出程序')
        exitAct.triggered.connect(qApp.quit)

        # 参数核查子菜单
        zteAct = QAction(QIcon(r'../Icon./中兴.png'), '中兴 (&Z)', self)
        # zetAct.setShortcut('Ctrl+Z')
        zteAct.setStatusTip('中兴参数核查')
        zteAct.setObjectName('zteAct')
        zteAct.triggered.connect(self.switch)

        huaweiAct = QAction(QIcon(r'../Icon/华为.png'), '华为 (&W)', self)
        huaweiAct.setStatusTip('华为参数核查')
        huaweiAct.setObjectName('huaweiAct')
        huaweiAct.triggered.connect(self.switch)

        # 工具子菜单栏
        seqAct = QAction(QIcon(r'../Icon/SEQ.png'),'SEQ话单分析', self)
        seqAct.setText('SEQ话单统计')
        seqAct.setObjectName('seqAct')
        seqAct.triggered.connect(self.switch)


        # *********************************  菜单栏  *********************************** #
        menubar = self.menuBar()
        # 文件
        fileMenu = menubar.addMenu('文件(&F)')
        fileMenu.addAction(homeAct)
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
        toolbar.addAction(homeAct)
        toolbar.addAction(zteAct)
        toolbar.addAction(huaweiAct)
        toolbar.addAction(seqAct)
        toolbar.addAction(exitAct)

        # 实例化一个QStackedWidget
        self.mainwidget = QStackedWidget()
        self.setCentralWidget(self.mainwidget)

        # 实例化分页面
        self.SEQ = SEQ_UI()

        self.HUAWEI = HUAWEI_UI()

        self.home1 = home()
        self.home = QWidget()
        self.home.setLayout(self.home1.layout1)

        self.zte1 = zte()
        self.zte = QWidget()
        self.zte.setLayout(self.zte1.layout_zte)

        # 将界面加入布局中
        self.mainwidget.addWidget(self.home)
        self.mainwidget.addWidget(self.SEQ)
        self.mainwidget.addWidget(self.zte)
        self.mainwidget.addWidget(self.HUAWEI)



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
            "homeAct": 0,
            "seqAct": 1,
            "zteAct": 2,
            "huaweiAct":3

        }
        print('索引：', index[sender])
        self.mainwidget.setCurrentIndex(index[sender])




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = main()
    # test_main.ui.show()
    main.show()
    sys.exit(app.exec_())
