import mysql.connector

# Pedir los datos desde la terminal
id_usuario = int(input("Ingresa el ID del usuario: "))
username = input("Ingresa el nombre de usuario: ")
password = input("Ingresa la contraseña: ")

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='negritorres1',
    database='jaguarete',
    port=3306
)

cursor = conexion.cursor()

# Sentencia SQL
sql = "INSERT INTO users (id, username, password) VALUES (%s, %s, %s)"
valores = (id_usuario, username, password)

try:
    cursor.execute(sql, valores)
    conexion.commit()
    print("Usuario insertado correctamente.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    conexion.rollback()

cursor.close()
conexion.close()
