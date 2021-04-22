import os
from PyQt5.QtWidgets import QWidget, QTreeWidget, QMdiArea, QTextEdit, QMdiSubWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
# 加载中兴的参数核查子选项
from ZX_X2 import X2

class zhongxing_main(QWidget):
    def __init__(self):
        super(zhongxing_main, self).__init__()
        self.initUI()

    def initUI(self):
        dir = os.path.abspath('..')
        self.ui = loadUi(r"{}/UI/zhongxing.ui".format(dir))
        # 加载lable
        self.ui.setWindowTitle("中兴")
        self.ui.setWindowIcon(QIcon(r'{}/Icon/中兴.png'.format(dir)))
        self.ui.treeWidget.clicked.connect(self.onTreeClicked)

    def onTreeClicked(self):
        item = self.ui.treeWidget.currentItem()
        click_name = item.text(0)
        if click_name == "LTEX2":
            print('LTEX2核查')
            self.subwin = X2()
            self.subwin.ui.show()

        elif click_name == 'LTE规划类参数':
            pass

        elif click_name == "LTE关键参数":
            print("正在核查关键参数")

        else:
            print('该功能暂时还未完成！')