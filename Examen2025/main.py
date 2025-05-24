from flask import Flask, request, jsonify
from cliente import obtener_cliente

app = Flask(__name__)

@app.route('/cliente', methods=['POST'])
def cliente():

    data = request.get_json()  
    ci = data.get("ci")  
    respuesta = obtener_cliente(ci)
    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True, port=5003)
