# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_user_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class edit_user_window(object):
    def setupUi(self, edit_user_window):
        if not edit_user_window.objectName():
            edit_user_window.setObjectName(u"edit_user_window")
        edit_user_window.resize(600, 630)
        edit_user_window.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.id_add_edit = QTextEdit(edit_user_window)
        self.id_add_edit.setObjectName(u"id_add_edit")
        self.id_add_edit.setGeometry(QRect(90, 140, 491, 31))
        font = QFont()
        font.setFamily(u"8514oem")
        font.setPointSize(8)
        self.id_add_edit.setFont(font)
        self.id_add_edit.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.add_edit_address_label = QLabel(edit_user_window)
        self.add_edit_address_label.setObjectName(u"add_edit_address_label")
        self.add_edit_address_label.setGeometry(QRect(20, 260, 221, 21))
        font1 = QFont()
        font1.setFamily(u"8514oem")
        self.add_edit_address_label.setFont(font1)
        self.add_edit_address_label.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.fecha_nacimiento_edit = QDateEdit(edit_user_window)
        self.fecha_nacimiento_edit.setObjectName(u"fecha_nacimiento_edit")
        self.fecha_nacimiento_edit.setGeometry(QRect(20, 370, 271, 31))
        self.fecha_nacimiento_edit.setFont(font1)
        self.fecha_nacimiento_edit.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.fecha_nacimiento_edit.setDate(QDate(2020, 1, 1))
        self.add_edit_name_label = QLabel(edit_user_window)
        self.add_edit_name_label.setObjectName(u"add_edit_name_label")
        self.add_edit_name_label.setGeometry(QRect(20, 190, 231, 21))
        self.add_edit_name_label.setFont(font1)
        self.add_edit_name_label.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.edit_user_city_label = QLabel(edit_user_window)
        self.edit_user_city_label.setObjectName(u"edit_user_city_label")
        self.edit_user_city_label.setGeometry(QRect(20, 420, 221, 21))
        self.edit_user_city_label.setFont(font1)
        self.edit_user_city_label.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.frame_add_client = QFrame(edit_user_window)
        self.frame_add_client.setObjectName(u"frame_add_client")
        self.frame_add_client.setGeometry(QRect(0, 0, 601, 101))
        self.frame_add_client.setFrameShape(QFrame.StyledPanel)
        self.frame_add_client.setFrameShadow(QFrame.Raised)
        self.Logo_edit = QPushButton(self.frame_add_client)
        self.Logo_edit.setObjectName(u"Logo_edit")
        self.Logo_edit.setGeometry(QRect(-10, 10, 371, 61))
        icon = QIcon()
        icon.addFile(u"./assets/images/logo-momentum.png", QSize(), QIcon.Normal, QIcon.On)
        self.Logo_edit.setIcon(icon)
        self.Logo_edit.setIconSize(QSize(300, 300))
        self.label_BD_ClientesEdit_2 = QLabel(self.frame_add_client)
        self.label_BD_ClientesEdit_2.setObjectName(u"label_BD_ClientesEdit_2")
        self.label_BD_ClientesEdit_2.setGeometry(QRect(350, 20, 231, 81))
        font2 = QFont()
        font2.setFamily(u"LEMON MILK Bold")
        font2.setPointSize(17)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setKerning(True)
        self.label_BD_ClientesEdit_2.setFont(font2)
        self.label_BD_ClientesEdit_2.setLayoutDirection(Qt.LeftToRight)
        self.label_BD_ClientesEdit_2.setAutoFillBackground(False)
        self.label_BD_ClientesEdit_2.setStyleSheet(u"background-color: rgb(30, 30,30);\n"
"color: rgb(242, 255, 76);")
        self.label_BD_ClientesEdit_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_BD_ClientesEdit_2.setWordWrap(True)
        self.label_BD_ClientesEdit_2.setMargin(0)
        self.label_BD_ClientesEdit_2.setIndent(-1)
        self.cost_edit = QTextEdit(edit_user_window)
        self.cost_edit.setObjectName(u"cost_edit")
        self.cost_edit.setGeometry(QRect(20, 540, 281, 31))
        self.cost_edit.setFont(font)
        self.cost_edit.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.edit_address = QTextEdit(edit_user_window)
        self.edit_address.setObjectName(u"edit_address")
        self.edit_address.setGeometry(QRect(20, 290, 271, 31))
        self.edit_address.setFont(font)
        self.edit_address.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.city_edit = QTextEdit(edit_user_window)
        self.city_edit.setObjectName(u"city_edit")
        self.city_edit.setGeometry(QRect(20, 460, 271, 31))
        self.city_edit.setFont(font)
        self.city_edit.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.add_edit_cost_label = QLabel(edit_user_window)
        self.add_edit_cost_label.setObjectName(u"add_edit_cost_label")
        self.add_edit_cost_label.setGeometry(QRect(20, 500, 221, 21))
        self.add_edit_cost_label.setFont(font1)
        self.add_edit_cost_label.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.add_user_base_frame = QFrame(edit_user_window)
        self.add_user_base_frame.setObjectName(u"add_user_base_frame")
        self.add_user_base_frame.setGeometry(QRect(0, 110, 591, 21))
        self.add_user_base_frame.setFrameShape(QFrame.StyledPanel)
        self.add_user_base_frame.setFrameShadow(QFrame.Raised)
        self.add_edit_id_label = QLabel(self.add_user_base_frame)
        self.add_edit_id_label.setObjectName(u"add_edit_id_label")
        self.add_edit_id_label.setGeometry(QRect(20, 0, 221, 21))
        self.add_edit_id_label.setFont(font1)
        self.add_edit_id_label.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.add_edit_phone_label = QLabel(edit_user_window)
        self.add_edit_phone_label.setObjectName(u"add_edit_phone_label")
        self.add_edit_phone_label.setGeometry(QRect(300, 260, 221, 21))
        self.add_edit_phone_label.setFont(font1)
        self.add_edit_phone_label.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.Filtrar_edit_id = QComboBox(edit_user_window)
        self.Filtrar_edit_id.addItem("")
        self.Filtrar_edit_id.addItem("")
        self.Filtrar_edit_id.addItem("")
        self.Filtrar_edit_id.setObjectName(u"Filtrar_edit_id")
        self.Filtrar_edit_id.setGeometry(QRect(20, 140, 61, 31))
        font3 = QFont()
        font3.setFamily(u"8514oem")
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setWeight(50)
        self.Filtrar_edit_id.setFont(font3)
        self.Filtrar_edit_id.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.cancel_edit = QPushButton(edit_user_window)
        self.cancel_edit.setObjectName(u"cancel_edit")
        self.cancel_edit.setGeometry(QRect(140, 580, 111, 28))
        self.cancel_edit.setFont(font1)
        self.cancel_edit.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u".assets/icons/2150373-social-media/png/025-log out.png", QSize(), QIcon.Normal, QIcon.On)
        self.cancel_edit.setIcon(icon1)
        self.name_edit = QTextEdit(edit_user_window)
        self.name_edit.setObjectName(u"name_edit")
        self.name_edit.setGeometry(QRect(20, 220, 561, 31))
        self.name_edit.setFont(font)
        self.name_edit.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.add_edit_date_label = QLabel(edit_user_window)
        self.add_edit_date_label.setObjectName(u"add_edit_date_label")
        self.add_edit_date_label.setGeometry(QRect(20, 340, 191, 21))
        self.add_edit_date_label.setFont(font1)
        self.add_edit_date_label.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.phone_edit = QTextEdit(edit_user_window)
        self.phone_edit.setObjectName(u"phone_edit")
        self.phone_edit.setGeometry(QRect(300, 290, 281, 31))
        self.phone_edit.setFont(font)
        self.phone_edit.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.Accept_edit = QPushButton(edit_user_window)
        self.Accept_edit.setObjectName(u"Accept_edit")
        self.Accept_edit.setGeometry(QRect(320, 580, 111, 28))
        self.Accept_edit.setFont(font1)
        self.Accept_edit.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u".assets/icons/2150373-social-media/png/024-log in.png", QSize(), QIcon.Normal, QIcon.On)
        self.Accept_edit.setIcon(icon2)
        self.edit_user_correo_label = QLabel(edit_user_window)
        self.edit_user_correo_label.setObjectName(u"edit_user_correo_label")
        self.edit_user_correo_label.setGeometry(QRect(300, 340, 221, 21))
        self.edit_user_correo_label.setFont(font1)
        self.edit_user_correo_label.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.correo_edit = QTextEdit(edit_user_window)
        self.correo_edit.setObjectName(u"correo_edit")
        self.correo_edit.setGeometry(QRect(300, 370, 281, 31))
        self.correo_edit.setFont(font)
        self.correo_edit.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.edit_user_comercial_label = QLabel(edit_user_window)
        self.edit_user_comercial_label.setObjectName(u"edit_user_comercial_label")
        self.edit_user_comercial_label.setGeometry(QRect(300, 420, 221, 21))
        self.edit_user_comercial_label.setFont(font1)
        self.edit_user_comercial_label.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.Filtrar_comercial_edit = QComboBox(edit_user_window)
        self.Filtrar_comercial_edit.addItem("")
        self.Filtrar_comercial_edit.addItem("")
        self.Filtrar_comercial_edit.addItem("")
        self.Filtrar_comercial_edit.setObjectName(u"Filtrar_comercial_edit")
        self.Filtrar_comercial_edit.setGeometry(QRect(300, 460, 281, 31))
        self.Filtrar_comercial_edit.setFont(font3)
        self.Filtrar_comercial_edit.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")

        self.retranslateUi(edit_user_window)

        QMetaObject.connectSlotsByName(edit_user_window)
    # setupUi

    def retranslateUi(self, edit_user_window):
        edit_user_window.setWindowTitle(QCoreApplication.translate("edit_user_window", u"Form", None))
        self.id_add_edit.setMarkdown("")
        self.id_add_edit.setHtml(QCoreApplication.translate("edit_user_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'8514oem'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.add_edit_address_label.setText(QCoreApplication.translate("edit_user_window", u"Direccion", None))
        self.add_edit_name_label.setText(QCoreApplication.translate("edit_user_window", u"Nombre Completo", None))
        self.edit_user_city_label.setText(QCoreApplication.translate("edit_user_window", u"Ciudad de Circulacion", None))
        self.Logo_edit.setText("")
        self.label_BD_ClientesEdit_2.setText(QCoreApplication.translate("edit_user_window", u"Editar Usuario", None))
        self.cost_edit.setMarkdown("")
        self.cost_edit.setHtml(QCoreApplication.translate("edit_user_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'8514oem'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.edit_address.setMarkdown("")
        self.edit_address.setHtml(QCoreApplication.translate("edit_user_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'8514oem'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.city_edit.setMarkdown("")
        self.city_edit.setHtml(QCoreApplication.translate("edit_user_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'8514oem'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.add_edit_cost_label.setText(QCoreApplication.translate("edit_user_window", u"Primas", None))
        self.add_edit_id_label.setText(QCoreApplication.translate("edit_user_window", u"Documento de Identidad", None))
        self.add_edit_phone_label.setText(QCoreApplication.translate("edit_user_window", u"Telefono", None))
        self.Filtrar_edit_id.setItemText(0, QCoreApplication.translate("edit_user_window", u"CC", None))
        self.Filtrar_edit_id.setItemText(1, QCoreApplication.translate("edit_user_window", u"CE", None))
        self.Filtrar_edit_id.setItemText(2, QCoreApplication.translate("edit_user_window", u"NIT", None))

        self.cancel_edit.setText(QCoreApplication.translate("edit_user_window", u"Cancelar", None))
        self.name_edit.setMarkdown("")
        self.name_edit.setHtml(QCoreApplication.translate("edit_user_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'8514oem'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.add_edit_date_label.setText(QCoreApplication.translate("edit_user_window", u"Fecha de Nacimiento", None))
        self.phone_edit.setMarkdown("")
        self.phone_edit.setHtml(QCoreApplication.translate("edit_user_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'8514oem'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Accept_edit.setText(QCoreApplication.translate("edit_user_window", u"Aceptar", None))
        self.edit_user_correo_label.setText(QCoreApplication.translate("edit_user_window", u"Correo Electronico", None))
        self.correo_edit.setMarkdown("")
        self.correo_edit.setHtml(QCoreApplication.translate("edit_user_window", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'8514oem'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.edit_user_comercial_label.setText(QCoreApplication.translate("edit_user_window", u"Comercial", None))
        self.Filtrar_comercial_edit.setItemText(0, QCoreApplication.translate("edit_user_window", u"Juan Miguel", None))
        self.Filtrar_comercial_edit.setItemText(1, QCoreApplication.translate("edit_user_window", u"Santiago", None))
        self.Filtrar_comercial_edit.setItemText(2, QCoreApplication.translate("edit_user_window", u"Cristina", None))

    # retranslateUi

