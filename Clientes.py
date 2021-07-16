import psycopg2 
from tkinter import ttk
from tkinter import *


#Constantes
PSQL_HOST = "localhost"
PSQL_PORT = "5432"
PSQL_USER = "postgres"
PSQL_PASS = "admin"
PSQL_DB = "BD_Momentum"

#Connection
connection_address = """
    host = %s port = %s user = %s password = %s dbname = %s
    """ % (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB) 


#connection = psycopg2.connect(connection_address)
#cursor = connection.cursor()

#Tkinter
class Cliente:
  #  connection_address = """
   # host = %s port = %s user = %s password = %s dbname = %s
    #""" % (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB) 

    def __init__(self, window):

        self.wind = window
        self.wind.title('Base de Datos Momentum')

        
        #Crear frame para cliente
        frame = LabelFrame(self.wind, text = "Registrar a un nuevo cliente")
        frame.grid(row = 0, column = 0, columnspan = 5, pady = 10)

        #Agregar cliente
        Label(frame, text = "Nombre: ").grid(row = 1, column = 0)
        self.nombre = Entry(frame)
        self.nombre.focus()
        self.nombre.grid(row = 1, column = 1) 

        Label(frame, text = 'Documento: ').grid(row = 2, column = 0)
        self.documento = Entry(frame)
        self.documento.grid(row = 2, column = 1)

        Label(frame, text = "Buscar Cliente: ").grid(row = 4, column = 0)
        self.busqueda = Entry(frame)
        self.busqueda
        self.busqueda.grid(row = 4, column = 1) 


        #Botones
        ttk.Button(frame, text = 'Guardar Cliente', command = self.add_cliente).grid(row = 3, columnspan = 2, sticky = W + E)
        ttk.Button(text = 'Borrar Cliente', command = self.delete_cliente).grid(row = 7, column = 0, sticky = W + E)
        ttk.Button(text = 'Editar Cliente', command = self.edit_cliente).grid(row = 7, column = 1, sticky = W + E)

        #Mensajes
        self.mensaje = Label(text = '', fg = 'red')
        self.mensaje.grid(row = 5, column = 0, columnspan = 2, sticky = W + E)

        #Tablas
        self.tabla = ttk.Treeview(height = 10 ,columns = ('#0','#1', '#2','#3', '#4', '#5'))
        self.tabla.grid(row = 6, column = 0, columnspan = 2)
        self.tabla.heading('#0', text = 'NOMBRE', anchor = W)
        self.tabla.heading('#1', text = 'TIPO DE DOCUMENTO', anchor = W)
        self.tabla.heading('#2', text = 'DOCUMENTO', anchor = W)
        self.tabla.heading('#3', text = 'TELEFONO', anchor = W)
        self.tabla.heading('#4', text = 'DIRECCIÓN', anchor = W)
        self.tabla.heading('#5', text = 'CORREO ELECTRÓNICO', anchor = W)
        self.tabla.heading('#6', text = 'COMERCIAL', anchor = W)
        

        #Llena las filas de las tablas
        self.get_clientes()
        

    #def run_query(self, query, parametros = ()):
    #    connection = psycopg2.connect(connection_address)
    #    cursor = connection.cursor()
    #    result = cursor.execute(query, parametros)
    #    connection.commit()   
    #    return result

    def get_connection(self, query, parametros = ()):
        connection = psycopg2.connect(connection_address)
        cursor = connection.cursor()
        cursor.execute(query, parametros)
        connection.commit()
        
        return cursor


    def get_clientes(self):
        query = 'SELECT nombre, t_documento ,documento, telefono, direccion, correo, comercial  FROM clientes'
        nombres = self.get_connection(query)
        #Limpiar la tabla
        records = self.tabla.get_children()
        for i in records:
            self.tabla.delete(i)
        #Datos
        for valores in nombres:
            print (valores)
            if valores == None:
                pass
            self.tabla.insert('', 0 , text = valores[0], values = (valores[1], valores[2], valores[3], valores[4], valores[5]))
            
            
            

    def validar(self):
        return len(self.nombre.get()) != 0 and len(self.documento.get()) != 0


    def add_cliente(self):
        if self.validar(): 
            query = 'INSERT INTO clientes VALUES(%s,NULL,%s)' 
            parametros = (self.documento.get(), self.nombre.get())
            self.get_connection(query, parametros)
            self.mensaje['text'] = 'Cliente {} agregado satisfactoriamente'.format(self.nombre.get())
            self.nombre.delete(0, END)
            self.documento.delete(0, END)
            print("Datos almacenados")  
        else:
            self.mensaje['text'] = 'Nombre y documento son requeridos'
            print("Necesario escribir el documento y el nombre")
        self.get_clientes()

    def delete_cliente(self):
        self.mensaje['text'] = ''
        try:
            self.tabla.item(self.tabla.selection())['text'][0]
        except IndexError as e:
            self.mensaje['text'] = 'Selecciona un producto'
            return
        self.mensaje['text'] = ''
        nombre = self.tabla.item(self.tabla.selection())['text']
        query = 'DELETE FROM clientes WHERE nombre = %s'
        self.get_connection(query, (nombre,))
        self.mensaje['text'] = 'Cliente {} fue borrado correctamente'.format(nombre)
        self.get_clientes()

    def edit_cliente(self):
        self.mensaje['text'] = ''
        try:
            self.tabla.item(self.tabla.selection())['text'][0]
        except IndexError as e:
            self.mensaje['text'] = 'Selecciona un producto'
            return
        nombre = self.tabla.item(self.tabla.selection())['text']
        documento = self.tabla.item(self.tabla.selection())['values'][0]
        self.ventana_edit = Toplevel()
        self.ventana_edit.title = 'Editar cliente'

        #Antiguo Nombre
        Label(self.ventana_edit, text = "Nombre Anterior: ").grid(row = 0, column = 1)
        Entry(self.ventana_edit, textvariable = StringVar(self.ventana_edit, value = nombre), state = 'readonly').grid(row = 0, column = 2)

        #Nuevo Nombre
        Label(self.ventana_edit, text = "Nuevo Nombre: ").grid(row = 1, column = 1)
        nuevo_nombre = Entry(self.ventana_edit)
        nuevo_nombre.grid(row = 1, column = 2)

        #Antiguo Documento
        Label(self.ventana_edit, text = "Documento Anterior: ").grid(row = 2, column = 1)
        Entry(self.ventana_edit, textvariable = StringVar(self.ventana_edit, value = documento), state = 'readonly').grid(row = 2, column = 2)

        #Nuevo Documento
        Label(self.ventana_edit, text = "Nuevo Documento: ").grid(row = 3, column = 1)
        nuevo_documento = Entry(self.ventana_edit)
        nuevo_documento.grid(row = 3, column = 2)

        Button(self.ventana_edit, text = "Actualizar", command = lambda: self.edit_informacion(nuevo_nombre.get(), nombre, nuevo_documento.get(), documento)).grid(row = 4, column = 2, sticky = W + E)
    
    def edit_informacion(self, n_nombre, v_nombre, n_documento, v_documento):
        query = 'UPDATE clientes SET nombre = %s, documento = %s WHERE nombre = %s AND documento = %s'
        parametros = (n_nombre, n_documento, v_nombre, v_documento)
        self.get_connection(query, parametros)
        self.ventana_edit.destroy()
        self.mensaje['text'] = 'El cliente {} fue actualizado de manera satisfactoria'.format(v_nombre)
        self.get_clientes()



if __name__ == '__main__':
    window = Tk()
    application = Cliente(window)
    window.mainloop()

'''
cursor.execute("SELECT id, documento, nombre  FROM clientes")

for id, documento, nombre in cursor.fetchall():
    print(id, documento, nombre)
    
'''


