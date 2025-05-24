from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Función para conectar a la base de datos y obtener los usuarios
def obtener_usuarios():
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='negritorres1',
        database='jaguarete',
        port=3306
    )
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    usuarios = cursor.fetchall()
    cursor.close()
    conexion.close()
    return usuarios

# Ruta API REST para obtener los usuarios
@app.route("/api/users", methods=["GET"])
def api_usuarios():
    usuarios = obtener_usuarios()
    return jsonify(usuarios)

# Ejecutar servidor
if __name__ == "__main__":
    app.run(debug=True)
