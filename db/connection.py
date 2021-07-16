import psycopg2 

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

def get_connection(query, parametros = ()):
        connection = psycopg2.connect(connection_address)
        cursor = connection.cursor()
        cursor.execute(query, parametros)
        connection.commit()
        
        return cursor
