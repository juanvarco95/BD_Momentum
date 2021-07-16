from PySide2.QtWidgets import QWidget, QFileDialog
from PySide2.QtCore import Qt
from views.add_user_window import add_user
from db.clientes import add_cliente


class AddClienteWindow(QWidget, add_user):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.accept_add_btn.clicked.connect(self.agregar_cliente)

    def check_inputs(self):
        type_id = self.Filtrar_id.currentText()
        id = self.id_add.toPlainText()
        nombre = self.name_add.toPlainText()
        direccion = self.address_add.toPlainText()
        telefono = self.phone_add.toPlainText()
        correo = self.correo_add_3.toPlainText()
        fecha = self.fecha_nacimiento_add.date().toString('dd-MM-yyyy')
        prima = self.primas_add_3.toPlainText()
        ciudad = self.city_add.toPlainText()

        c_errors = 0

        if id == "":
            print("Falta ingresar el documento")
            c_errors += 1
        if nombre == "":
            print("Falta ingresar el nombre")
            c_errors += 1
        if direccion == "":
            print("Falta ingresar el direccion")
            c_errors += 1
        if telefono == "":
            print("Falta ingresar el telefono")
            c_errors += 1
        if ciudad == "":
            print("Falta ingresar la ciudad")
            c_errors += 1
        if correo == "":
            print("Falta ingresar el correo")
            c_errors += 1

        if c_errors == 0:
            return True

    def agregar_cliente(self):
        type_id = self.Filtrar_id.currentText()
        id = self.id_add.toPlainText()
        nombre = self.name_add.toPlainText()
        direccion = self.address_add.toPlainText()
        telefono = self.phone_add.toPlainText()
        correo = self.correo_add_3.toPlainText()
        comercial = self.Filtrar_comercial.currentText()
        fecha = self.fecha_nacimiento_add.date().toString('dd-MM-yyyy')
        prima = self.primas_add_3.toPlainText()
        ciudad = self.city_add.toPlainText()

        if self.check_inputs():
            parametros = id, type_id, nombre, telefono, correo, direccion,fecha,comercial, prima, ciudad
            add_cliente(parametros)
            self.clean_inputs()
        

    def clean_inputs(self):
        self.id_add.clear()
        self.name_add.clear()
        self.address_add.clear()
        self.phone_add.clear()
        self.fecha_nacimiento_add.clear()
        self.primas_add_3.clear()
        self.city_add.clear()
        

   