# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pdf_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_pdf_create(object):
    def setupUi(self, pdf_create):
        if not pdf_create.objectName():
            pdf_create.setObjectName(u"pdf_create")
        pdf_create.resize(600, 360)
        pdf_create.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame = QFrame(pdf_create)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 601, 101))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_PDF = QFrame(self.frame)
        self.frame_PDF.setObjectName(u"frame_PDF")
        self.frame_PDF.setGeometry(QRect(0, 0, 601, 101))
        self.frame_PDF.setFrameShape(QFrame.StyledPanel)
        self.frame_PDF.setFrameShadow(QFrame.Raised)
        self.Logo_3 = QPushButton(self.frame_PDF)
        self.Logo_3.setObjectName(u"Logo_3")
        self.Logo_3.setGeometry(QRect(-10, 10, 371, 61))
        icon = QIcon()
        icon.addFile(u"../assets/images/logo-momentum.png", QSize(), QIcon.Normal, QIcon.On)
        self.Logo_3.setIcon(icon)
        self.Logo_3.setIconSize(QSize(300, 300))
        self.label_BD_Clientes_3 = QLabel(self.frame_PDF)
        self.label_BD_Clientes_3.setObjectName(u"label_BD_Clientes_3")
        self.label_BD_Clientes_3.setGeometry(QRect(330, 10, 271, 81))
        font = QFont()
        font.setFamily(u"LEMON MILK Bold")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_BD_Clientes_3.setFont(font)
        self.label_BD_Clientes_3.setLayoutDirection(Qt.LeftToRight)
        self.label_BD_Clientes_3.setAutoFillBackground(False)
        self.label_BD_Clientes_3.setStyleSheet(u"background-color: rgb(0, 0,0);\n"
"color: rgb(76, 108, 255);")
        self.label_BD_Clientes_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_BD_Clientes_3.setWordWrap(True)
        self.label_BD_Clientes_3.setMargin(0)
        self.label_BD_Clientes_3.setIndent(-1)
        self.frame_2 = QFrame(pdf_create)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 70, 601, 221))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.add_user_id_label = QLabel(self.frame_2)
        self.add_user_id_label.setObjectName(u"add_user_id_label")
        self.add_user_id_label.setGeometry(QRect(20, 50, 221, 21))
        font1 = QFont()
        font1.setFamily(u"8514oem")
        self.add_user_id_label.setFont(font1)
        self.add_user_id_label.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.add_user_id_label_2 = QLabel(self.frame_2)
        self.add_user_id_label_2.setObjectName(u"add_user_id_label_2")
        self.add_user_id_label_2.setGeometry(QRect(320, 50, 221, 21))
        self.add_user_id_label_2.setFont(font1)
        self.add_user_id_label_2.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.fecha_nacimiento_add_2 = QDateEdit(self.frame_2)
        self.fecha_nacimiento_add_2.setObjectName(u"fecha_nacimiento_add_2")
        self.fecha_nacimiento_add_2.setGeometry(QRect(20, 150, 281, 31))
        self.fecha_nacimiento_add_2.setFont(font1)
        self.fecha_nacimiento_add_2.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.fecha_nacimiento_add_2.setDate(QDate(2020, 1, 1))
        self.id_add_5 = QTextEdit(self.frame_2)
        self.id_add_5.setObjectName(u"id_add_5")
        self.id_add_5.setGeometry(QRect(20, 80, 281, 31))
        font2 = QFont()
        font2.setFamily(u"8514oem")
        font2.setPointSize(8)
        self.id_add_5.setFont(font2)
        self.id_add_5.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.id_add_6 = QTextEdit(self.frame_2)
        self.id_add_6.setObjectName(u"id_add_6")
        self.id_add_6.setGeometry(QRect(320, 80, 271, 31))
        self.id_add_6.setFont(font2)
        self.id_add_6.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.id_add_7 = QTextEdit(self.frame_2)
        self.id_add_7.setObjectName(u"id_add_7")
        self.id_add_7.setGeometry(QRect(320, 150, 271, 31))
        self.id_add_7.setFont(font2)
        self.id_add_7.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.add_user_id_label_3 = QLabel(self.frame_2)
        self.add_user_id_label_3.setObjectName(u"add_user_id_label_3")
        self.add_user_id_label_3.setGeometry(QRect(20, 120, 221, 21))
        self.add_user_id_label_3.setFont(font1)
        self.add_user_id_label_3.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.add_user_id_label_4 = QLabel(self.frame_2)
        self.add_user_id_label_4.setObjectName(u"add_user_id_label_4")
        self.add_user_id_label_4.setGeometry(QRect(320, 120, 221, 21))
        self.add_user_id_label_4.setFont(font1)
        self.add_user_id_label_4.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3 = QPushButton(pdf_create)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(340, 300, 111, 28))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u"../assets/icons/2150373-social-media/png/024-log in.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_4 = QPushButton(pdf_create)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(170, 300, 111, 28))
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u"../assets/icons/2150373-social-media/png/025-log out.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_4.setIcon(icon2)

        self.retranslateUi(pdf_create)

        QMetaObject.connectSlotsByName(pdf_create)
    # setupUi

    def retranslateUi(self, pdf_create):
        pdf_create.setWindowTitle(QCoreApplication.translate("pdf_create", u"Form", None))
        self.Logo_3.setText("")
        self.label_BD_Clientes_3.setText(QCoreApplication.translate("pdf_create", u"Generar PDF", None))
        self.add_user_id_label.setText(QCoreApplication.translate("pdf_create", u"Nombre", None))
        self.add_user_id_label_2.setText(QCoreApplication.translate("pdf_create", u"Placa", None))
        self.id_add_5.setMarkdown("")
        self.id_add_5.setHtml(QCoreApplication.translate("pdf_create", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'8514oem'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.id_add_6.setMarkdown("")
        self.id_add_6.setHtml(QCoreApplication.translate("pdf_create", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'8514oem'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.id_add_7.setMarkdown("")
        self.id_add_7.setHtml(QCoreApplication.translate("pdf_create", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'8514oem'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.add_user_id_label_3.setText(QCoreApplication.translate("pdf_create", u"Fecha", None))
        self.add_user_id_label_4.setText(QCoreApplication.translate("pdf_create", u"Precio", None))
        self.pushButton_3.setText(QCoreApplication.translate("pdf_create", u"Aceptar", None))
        self.pushButton_4.setText(QCoreApplication.translate("pdf_create", u"Cancelar", None))
    # retranslateUi

