import psycopg2
from .connection import get_connection

def get_clientes():
        query = 'SELECT nombre, t_documento ,documento, telefono, direccion, correo, ciudad_circulacion, fecha_nacimiento, comercial, primas FROM clientes'
        cursor = get_connection(query)
        return cursor

def get_clientes_by_id(_id):
        query = f'SELECT nombre, t_documento ,documento, telefono, direccion, correo, ciudad_circulacion, fecha_nacimiento, comercial, primas  FROM clientes WHERE documento = {_id}'
        get_connection(query, _id)

def get_clientes_by_nombre(nombre):
        query = f'SELECT nombre, t_documento ,documento, telefono, direccion, correo, ciudad_circulacion, fecha_nacimiento, comercial, primas FROM clientes WHERE nombre LIKE '%{nombre}%' '
        get_connection(query, nombre)
    
def get_clientes_by_fecha(fecha):
        query = f'SELECT nombre, t_documento ,documento, telefono, direccion, correo, ciudad_circulacion, fecha_nacimiento, comercial, primas FROM clientes WHERE nombre LIKE '%{fecha}%' '
        get_connection(query, fecha)
        
def create_pdf():
    pass
            
def add_cliente(parametros):
    query = 'INSERT INTO clientes VALUES(%s,%s,%s,%s,%s,%s,%s,%s,NULL,NULL,%s,NULL,%s)' 
    get_connection(query, parametros)
    print("Datos almacenados")  
    get_clientes()
                  



def edit_cliente(_id, parametros):
    query = f'UPDATE clientes SET nombre = %s, documento = %s, t_documento = %s, telefono = %s, direccion = %s, correo = %s, ciudad_circulacion WHERE documento = {_id}' 
    get_connection(query, parametros)
    print("Datos almacenados")  
    get_clientes()        
   
def delete_cliente(_id):
    query = 'DELETE FROM clientes WHERE documento = {_id}'
    get_connection(query)
   


'''
def delete_cliente():
    #mensaje['text'] = ''
    #try:
        #.tabla.item(.tabla.selection())['text'][0]
    #except IndexError as e:
       # mensaje['text'] = 'Selecciona un producto'
            return
        #mensaje['text'] = ''
        nombre = .tabla.item(.tabla.selection())['text']
        query = 'DELETE FROM clientes WHERE nombre = %s'
        .get_connection(query, (nombre,))
        .mensaje['text'] = 'Cliente {} fue borrado correctamente'.format(nombre)
        .get_clientes()

    def edit_cliente():
        .mensaje['text'] = ''
        try:
            .tabla.item(.tabla.selection())['text'][0]
        except IndexError as e:
            .mensaje['text'] = 'Selecciona un producto'
            return
        nombre = .tabla.item(.tabla.selection())['text']
        documento = .tabla.item(.tabla.selection())['values'][0]
        .ventana_edit = Toplevel()
        .ventana_edit.title = 'Editar cliente'
'''