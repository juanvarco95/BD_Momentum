from PySide2.QtWidgets import QTableWidgetItem, QWidget
from views.main_window import List_Cliente
from controllers.add_user_window import AddClienteWindow
from controllers.edit_user_window import EditUserWindow
from controllers.pdf_window import PDFWindow
from db.clientes import get_clientes
from db.connection import get_connection

class ListClienteWindow(QWidget, List_Cliente):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)   
        self.add_cliente.clicked.connect(self.open_new_client_window)
        self.edit_cliente.clicked.connect(self.open_edit_client_window)
        self.add_pdf.clicked.connect(self.open_PDF_window)
        self.populate_table()
        self.table_config()
        
    
    def open_new_client_window(self):
        window = AddClienteWindow(self)
        window.show()
    
    def open_edit_client_window(self):
        window = EditUserWindow(self)
        window.show()
    
    def open_PDF_window(self):
        window = PDFWindow(self)
        window.show()

    def remove_client(self):
        pass

    def table_config(self):
        column_headers = {"Nombre", "Tipo de Documento" ,"Documento", "Telefono", "Direccion", "Correo", "Ciudad de Circulacion", "Fecha de Nacimiento", "Comercial", "Primas"}
        self.table_clientes.setColumnCount(len(column_headers))
        self.table_clientes.setHorizontalHeaderLabels(column_headers)

    def populate_table(self):
        query = 'SELECT nombre, t_documento ,documento, telefono, direccion, correo, ciudad_circulacion, fecha_nacimiento, comercial, primas FROM clientes'
        nombres = get_connection(query)
        #print (nombres.fetchall())
        lista = nombres.fetchall()
        self.table_clientes.setRowCount(len(lista))
        fila = 0
        for registro in lista:
            columna = 0
            self.table_clientes.insertRow(fila)
            for elemento in registro:
                celda = QTableWidgetItem(elemento)
                self.table_clientes.setItem(fila, columna, celda)
                columna += 1
            fila += 1
           
       # self.table_clientes.setItem(1, 1, QTableWidgetItem(nombres[5]))
        #self.table_clientes.setItem(2, 1, QTableWidgetItem("Hola"))
     
            
        
        


            
    def populate_combobox(self):
        pass

    def search(self):
        pass

    def records(self):
        pass