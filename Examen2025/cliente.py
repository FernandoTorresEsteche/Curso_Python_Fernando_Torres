clientes_db = {
    "4133266": {"ci": "4133266"},

}
def obtener_cliente(ci):
    if ci in clientes_db:
        return {
            "accion": "Success", 
            "codRes": "SIN_ERROR", 
            "menRes": "OK", 
            "ci": ci
        }
    else:
        return {
            "accion": "Cliente no está en el sistema", 
            "codRes": "ERROR", 
            "menRes": "Error cliente", 
            "ci": ci
        }    
