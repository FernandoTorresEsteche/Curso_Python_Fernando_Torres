from flask import Blueprint, request, jsonify

cliente = Blueprint('cliente', __name__)

@cliente.route('/cliente', methods=['POST'])
def llamarServicioSet():
    ci = request.json.get('ci')

    codRes, menRes, accion = inicializarVariables(ci)

    salida = {
        'codRes': codRes,
        'menRes': menRes,
        'ci': ci,
        'accion': accion
    }
    return jsonify(salida)

def inicializarVariables(ci):
    cilocal = "4133266"
    codRes = 'SIN_ERROR'
    menRes = 'OK'

    try:
        print("Verificar login")
        if ci == cilocal:
            print("Success")
            accion = "Success"
        else:
            print("Cliente no está en el sistema")
            accion = "Cliente no está en el sistema"
            codRes = 'ERROR'
            menRes = 'Error cliente'


    except Exception as e:
        print("ERROR", str(e))
        codRes = 'ERROR'
        menRes = 'Msg:' + str(e)
        accion = "Error interno"

    return codRes, menRes, accion
            
