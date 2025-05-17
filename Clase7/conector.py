import mysql.connector
from mysql.connector import Error

def conectar_mysql():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='negritorres1',                        
            database='jaguarete',
            port=3306,
        )

        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            cursor = conexion.cursor()
            cursor.execute("SELECT DATABASE();")
            resultado = cursor.fetchone()
            print("Conectado a la base de datos:", resultado)
     
    except Error as e:
            print("Error al conectar a la base de datos:", e)
    finally:
        if 'conexion' in locals() and conexion.is_connected():
                conexion.close()
                print("Conexión cerrada")

if __name__ == "__main__":
    conectar_mysql()

            