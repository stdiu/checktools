# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'huawei.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(651, 447)
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 161, 441))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.treeWidget.headerItem().setText(0, _translate("Form", "参数类型"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Form", "4G"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("Form", "规划类参数"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("Form", "关键参数"))
        self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("Form", "PCI混淆"))
        self.treeWidget.topLevelItem(0).child(3).setText(0, _translate("Form", "功率和工控"))
        self.treeWidget.topLevelItem(0).child(4).setText(0, _translate("Form", "切换重选"))
        self.treeWidget.topLevelItem(0).child(5).setText(0, _translate("Form", "异频频点"))
        self.treeWidget.topLevelItem(0).child(6).setText(0, _translate("Form", "外部小区"))
        self.treeWidget.topLevelItem(0).child(7).setText(0, _translate("Form", "邻接关系"))
        self.treeWidget.topLevelItem(0).child(8).setText(0, _translate("Form", "邻区一致性"))
        self.treeWidget.topLevelItem(0).child(9).setText(0, _translate("Form", "X2"))
        self.treeWidget.topLevelItem(0).child(10).setText(0, _translate("Form", "锚点关键参数"))
        self.treeWidget.topLevelItem(0).child(11).setText(0, _translate("Form", "锚点优选"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Form", "5G"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("Form", "规划类参数"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("Form", "PCI混淆"))
        self.treeWidget.topLevelItem(1).child(2).setText(0, _translate("Form", "关键参数"))
        self.treeWidget.topLevelItem(1).child(3).setText(0, _translate("Form", "邻区一致性"))
        self.treeWidget.topLevelItem(1).child(4).setText(0, _translate("Form", "XN"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
