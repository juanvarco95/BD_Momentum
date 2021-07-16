# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mian_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_List_Cliente(object):
    def setupUi(self, List_Cliente):
        if not List_Cliente.objectName():
            List_Cliente.setObjectName(u"List_Cliente")
        List_Cliente.resize(900, 600)
        self.Button = QPushButton(List_Cliente)
        self.Button.setObjectName(u"Button")
        self.Button.setGeometry(QRect(440, 280, 121, 41))

        self.retranslateUi(List_Cliente)

        QMetaObject.connectSlotsByName(List_Cliente)
    # setupUi

    def retranslateUi(self, List_Cliente):
        List_Cliente.setWindowTitle(QCoreApplication.translate("List_Cliente", u"BD Momentum", None))
        self.Button.setText(QCoreApplication.translate("List_Cliente", u"PushButton", None))
    # retranslateUi

