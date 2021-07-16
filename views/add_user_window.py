# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_user_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class add_user(object):
    def setupUi(self, add_user):
        if not add_user.objectName():
            add_user.setObjectName(u"add_user")
        add_user.resize(600, 630)
        add_user.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.frame_add_client = QFrame(add_user)
        self.frame_add_client.setObjectName(u"frame_add_client")
        self.frame_add_client.setGeometry(QRect(0, 0, 600, 100))
        self.frame_add_client.setFrameShape(QFrame.StyledPanel)
        self.frame_add_client.setFrameShadow(QFrame.Raised)
        self.Logo_2 = QPushButton(self.frame_add_client)
        self.Logo_2.setObjectName(u"Logo_2")
        self.Logo_2.setGeometry(QRect(-10, 10, 371, 61))
        icon = QIcon()
        icon.addFile(u"./assets/images/logo-momentum.png", QSize(), QIcon.Normal, QIcon.On)
        self.Logo_2.setIcon(icon)
        self.Logo_2.setIconSize(QSize(300, 300))
        self.label_BD_Clientes_2 = QLabel(self.frame_add_client)
        self.label_BD_Clientes_2.setObjectName(u"label_BD_Clientes_2")
        self.label_BD_Clientes_2.setGeometry(QRect(330, 10, 271, 81))
        font = QFont()
        font.setFamily(u"LEMON MILK Bold")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_BD_Clientes_2.setFont(font)
        self.label_BD_Clientes_2.setLayoutDirection(Qt.LeftToRight)
        self.label_BD_Clientes_2.setAutoFillBackground(False)
        self.label_BD_Clientes_2.setStyleSheet(u"background-color: rgb(30, 30,30);\n"
"color: rgb(100, 252, 196);")
        self.label_BD_Clientes_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_BD_Clientes_2.setWordWrap(True)
        self.label_BD_Clientes_2.setMargin(0)
        self.label_BD_Clientes_2.setIndent(-1)
        self.Filtrar_id = QComboBox(add_user)
        self.Filtrar_id.addItem("")
        self.Filtrar_id.addItem("")
        self.Filtrar_id.addItem("")
        self.Filtrar_id.setObjectName(u"Filtrar_id")
        self.Filtrar_id.setGeometry(QRect(20, 140, 61, 31))
        font1 = QFont()
        font1.setFamily(u"8514oem")
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setWeight(50)
        self.Filtrar_id.setFont(font1)
        self.Filtrar_id.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.id_add = QTextEdit(add_user)
        self.id_add.setObjectName(u"id_add")
        self.id_add.setGeometry(QRect(90, 140, 491, 31))
        font2 = QFont()
        font2.setFamily(u"8514oem")
        font2.setPointSize(8)
        self.id_add.setFont(font2)
        self.id_add.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.name_add = QTextEdit(add_user)
        self.name_add.setObjectName(u"name_add")
        self.name_add.setGeometry(QRect(20, 220, 561, 31))
        self.name_add.setFont(font2)
        self.name_add.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.address_add = QTextEdit(add_user)
        self.address_add.setObjectName(u"address_add")
        self.address_add.setGeometry(QRect(20, 290, 271, 31))
        self.address_add.setFont(font2)
        self.address_add.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.phone_add = QTextEdit(add_user)
        self.phone_add.setObjectName(u"phone_add")
        self.phone_add.setGeometry(QRect(300, 290, 281, 31))
        self.phone_add.setFont(font2)
        self.phone_add.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.fecha_nacimiento_add = QDateEdit(add_user)
        self.fecha_nacimiento_add.setObjectName(u"fecha_nacimiento_add")
        self.fecha_nacimiento_add.setGeometry(QRect(20, 370, 271, 31))
        font3 = QFont()
        font3.setFamily(u"8514oem")
        self.fecha_nacimiento_add.setFont(font3)
        self.fecha_nacimiento_add.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.fecha_nacimiento_add.setDate(QDate(2020, 1, 1))
        self.add_user_date_label = QLabel(add_user)
        self.add_user_date_label.setObjectName(u"add_user_date_label")
        self.add_user_date_label.setGeometry(QRect(20, 340, 191, 21))
        self.add_user_date_label.setFont(font3)
        self.add_user_date_label.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.add_user_name_label = QLabel(add_user)
        self.add_user_name_label.setObjectName(u"add_user_name_label")
        self.add_user_name_label.setGeometry(QRect(20, 190, 231, 21))
        self.add_user_name_label.setFont(font3)
        self.add_user_name_label.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.add_user_address_label = QLabel(add_user)
        self.add_user_address_label.setObjectName(u"add_user_address_label")
        self.add_user_address_label.setGeometry(QRect(20, 260, 221, 21))
        self.add_user_address_label.setFont(font3)
        self.add_user_address_label.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.add_user_phone_label = QLabel(add_user)
        self.add_user_phone_label.setObjectName(u"add_user_phone_label")
        self.add_user_phone_label.setGeometry(QRect(300, 260, 221, 21))
        self.add_user_phone_label.setFont(font3)
        self.add_user_phone_label.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.add_user_city_label = QLabel(add_user)
        self.add_user_city_label.setObjectName(u"add_user_city_label")
        self.add_user_city_label.setGeometry(QRect(20, 420, 221, 21))
        self.add_user_city_label.setFont(font3)
        self.add_user_city_label.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.city_add = QTextEdit(add_user)
        self.city_add.setObjectName(u"city_add")
        self.city_add.setGeometry(QRect(20, 460, 271, 31))
        self.city_add.setFont(font2)
        self.city_add.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.cancel_add_btn = QPushButton(add_user)
        self.cancel_add_btn.setObjectName(u"cancel_add_btn")
        self.cancel_add_btn.setGeometry(QRect(150, 580, 111, 28))
        self.cancel_add_btn.setFont(font3)
        self.cancel_add_btn.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/2150373-social-media/png/025-log out.png", QSize(), QIcon.Normal, QIcon.On)
        self.cancel_add_btn.setIcon(icon1)
        self.accept_add_btn = QPushButton(add_user)
        self.accept_add_btn.setObjectName(u"accept_add_btn")
        self.accept_add_btn.setGeometry(QRect(320, 580, 111, 28))
        self.accept_add_btn.setFont(font3)
        self.accept_add_btn.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/2150373-social-media/png/024-log in.png", QSize(), QIcon.Normal, QIcon.On)
        self.accept_add_btn.setIcon(icon2)
        self.add_user_id_label = QLabel(add_user)
        self.add_user_id_label.setObjectName(u"add_user_id_label")
        self.add_user_id_label.setGeometry(QRect(10, 100, 221, 21))
        self.add_user_id_label.setFont(font3)
        self.add_user_id_label.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.add_user_base_frame_2 = QFrame(add_user)
        self.add_user_base_frame_2.setObjectName(u"add_user_base_frame_2")
        self.add_user_base_frame_2.setGeometry(QRect(0, 110, 591, 461))
        self.add_user_base_frame_2.setFrameShape(QFrame.StyledPanel)
        self.add_user_base_frame_2.setFrameShadow(QFrame.Raised)
        self.add_user_comercial_label_4 = QLabel(self.add_user_base_frame_2)
        self.add_user_comercial_label_4.setObjectName(u"add_user_comercial_label_4")
        self.add_user_comercial_label_4.setGeometry(QRect(300, 310, 221, 21))
        self.add_user_comercial_label_4.setFont(font3)
        self.add_user_comercial_label_4.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.Filtrar_comercial = QComboBox(self.add_user_base_frame_2)
        self.Filtrar_comercial.addItem("")
        self.Filtrar_comercial.addItem("")
        self.Filtrar_comercial.addItem("")
        self.Filtrar_comercial.setObjectName(u"Filtrar_comercial")
        self.Filtrar_comercial.setGeometry(QRect(300, 350, 281, 31))
        self.Filtrar_comercial.setFont(font1)
        self.Filtrar_comercial.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.add_user_correo_label_5 = QLabel(self.add_user_base_frame_2)
        self.add_user_correo_label_5.setObjectName(u"add_user_correo_label_5")
        self.add_user_correo_label_5.setGeometry(QRect(300, 230, 221, 21))
        self.add_user_correo_label_5.setFont(font3)
        self.add_user_correo_label_5.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.correo_add_3 = QTextEdit(self.add_user_base_frame_2)
        self.correo_add_3.setObjectName(u"correo_add_3")
        self.correo_add_3.setGeometry(QRect(300, 260, 281, 31))
        self.correo_add_3.setFont(font2)
        self.correo_add_3.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.primas_add_3 = QTextEdit(self.add_user_base_frame_2)
        self.primas_add_3.setObjectName(u"primas_add_3")
        self.primas_add_3.setGeometry(QRect(20, 420, 281, 31))
        self.primas_add_3.setFont(font2)
        self.primas_add_3.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.add_user_cost_label_3 = QLabel(self.add_user_base_frame_2)
        self.add_user_cost_label_3.setObjectName(u"add_user_cost_label_3")
        self.add_user_cost_label_3.setGeometry(QRect(20, 390, 221, 21))
        self.add_user_cost_label_3.setFont(font3)
        self.add_user_cost_label_3.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.add_user_base_frame_2.raise_()
        self.frame_add_client.raise_()
        self.Filtrar_id.raise_()
        self.id_add.raise_()
        self.name_add.raise_()
        self.address_add.raise_()
        self.phone_add.raise_()
        self.fecha_nacimiento_add.raise_()
        self.add_user_date_label.raise_()
        self.add_user_name_label.raise_()
        self.add_user_address_label.raise_()
        self.add_user_phone_label.raise_()
        self.add_user_city_label.raise_()
        self.city_add.raise_()
        self.cancel_add_btn.raise_()
        self.accept_add_btn.raise_()
        self.add_user_id_label.raise_()

        self.retranslateUi(add_user)

        QMetaObject.connectSlotsByName(add_user)
    # setupUi

    def retranslateUi(self, add_user):
        add_user.setWindowTitle(QCoreApplication.translate("add_user", u"Form", None))
        self.Logo_2.setText("")
        self.label_BD_Clientes_2.setText(QCoreApplication.translate("add_user", u"Agregar Usuario", None))
        self.Filtrar_id.setItemText(0, QCoreApplication.translate("add_user", u"CC", None))
        self.Filtrar_id.setItemText(1, QCoreApplication.translate("add_user", u"CE", None))
        self.Filtrar_id.setItemText(2, QCoreApplication.translate("add_user", u"NIT", None))

        self.id_add.setMarkdown("")
        self.id_add.setHtml(QCoreApplication.translate("add_user", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'8514oem'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.name_add.setMarkdown("")
        self.name_add.setHtml(QCoreApplication.translate("add_user", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'8514oem'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.address_add.setMarkdown("")
        self.address_add.setHtml(QCoreApplication.translate("add_user", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'8514oem'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.phone_add.setMarkdown("")
        self.phone_add.setHtml(QCoreApplication.translate("add_user", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'8514oem'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.add_user_date_label.setText(QCoreApplication.translate("add_user", u"Fecha de Nacimiento", None))
        self.add_user_name_label.setText(QCoreApplication.translate("add_user", u"Nombre Completo", None))
        self.add_user_address_label.setText(QCoreApplication.translate("add_user", u"Direccion", None))
        self.add_user_phone_label.setText(QCoreApplication.translate("add_user", u"Telefono", None))
        self.add_user_city_label.setText(QCoreApplication.translate("add_user", u"Ciudad de Circulacion", None))
        self.city_add.setMarkdown("")
        self.city_add.setHtml(QCoreApplication.translate("add_user", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'8514oem'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.cancel_add_btn.setText(QCoreApplication.translate("add_user", u"Cancelar", None))
        self.accept_add_btn.setText(QCoreApplication.translate("add_user", u"Aceptar", None))
        self.add_user_id_label.setText(QCoreApplication.translate("add_user", u"Documento de Identidad", None))
        self.add_user_comercial_label_4.setText(QCoreApplication.translate("add_user", u"Comercial", None))
        self.Filtrar_comercial.setItemText(0, QCoreApplication.translate("add_user", u"Juan Miguel", None))
        self.Filtrar_comercial.setItemText(1, QCoreApplication.translate("add_user", u"Santiago", None))
        self.Filtrar_comercial.setItemText(2, QCoreApplication.translate("add_user", u"Cristina", None))

        self.add_user_correo_label_5.setText(QCoreApplication.translate("add_user", u"Correo Electronico", None))
        self.correo_add_3.setMarkdown("")
        self.correo_add_3.setHtml(QCoreApplication.translate("add_user", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'8514oem'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.primas_add_3.setMarkdown("")
        self.primas_add_3.setHtml(QCoreApplication.translate("add_user", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'8514oem'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.add_user_cost_label_3.setText(QCoreApplication.translate("add_user", u"Primas", None))
    # retranslateUi

