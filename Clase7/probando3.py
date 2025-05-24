from flask import Flask, render_template_string
import mysql.connector

app = Flask(__name__)

# Conexión a la base de datos
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

# Ruta principal
@app.route("/")
def mostrar_usuarios():
    usuarios = obtener_usuarios()
    return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Lista de Usuarios</title>
            <style>
                body { font-family: Arial; background: #f2f2f2; padding: 20px; }
                table { border-collapse: collapse; width: 50%; margin: auto; background: white; }
                th, td { border: 1px solid #ccc; padding: 10px; text-align: left; }
                th { background-color: #eee; }
                h1 { text-align: center; }
            </style>
        </head>
        <body>
            <h1>Usuarios Registrados</h1>
            <table>
                <tr><th>ID</th><th>Username</th><th>Password</th></tr>
                {% for usuario in usuarios %}
                <tr>
                    <td>{{ usuario.id }}</td>
                    <td>{{ usuario.username }}</td>
                    <td>{{ usuario.password }}</td>
                </tr>
                {% endfor %}
            </table>
        </body>
        </html>
    """, usuarios=usuarios)

# Ejecutar la app
if __name__ == "__main__":
    app.run(debug=True)
