from flask import Blueprint, jsonify, request
import mysql.connector
from mysql.connector import Error

login_bp = Blueprint('login', __name__)
@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    codRes, menRes, accion, usuario = verficar_credenciales(username, password)

    return jsonify({
        'codigo': codRes,
        'mensaje': menRes,
        'accion': accion,
        'usuario': usuario
    })

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'negritorres1',
    'database': 'jaguarete',    
}

def verficar_credenciales(user, password):
    codRes ='SIN_ERROR'
    menRes ='OK'
    usuario = None
    
    try:
        print("Verificar login")
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)
        
        query = "SELECT  username FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (user, password))
        
        result = cursor.fetchone()
        
        if result: 
            usuario = result['username']
            print("Usuario y contraseña Ok")
            accion = 'LOGIN_OK'
        else:
            print("Usuario o contraseña incorrectos")
            accion = 'LOGIN_ERROR'
            codRes = 'ERROR_LOGIN'
            menRes = 'Usuario o contraseña incorrectos'
            
        cursor.close()
        connection.close()
    except Error as e:
        print("ERROR",str(e))
        codRes = 'ERROR_DB'
        menRes = 'Msg: ' + str(e)
        accion = 'LOGIN_ERROR'
    return codRes, menRes, accion, usuario 