import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='negritorres1',
    database='jaguarete',
    port=3306
)

# Crear cursor para ejecutar sentencias SQL
cursor = conexion.cursor()

# Sentencia SQL para insertar datos
sql = "INSERT INTO users (id, username, password) VALUES (%s, %s, %s)"
valores = (4, 'user4', 'password4')

try:
    cursor.execute(sql, valores)
    conexion.commit()
    print("Datos insertados correctamente.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    conexion.rollback()

# Cerrar conexión
cursor.close()
conexion.close()
print("Conexión cerrada.")