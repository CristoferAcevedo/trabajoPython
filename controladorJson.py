import json
#from modeloJson import modeloFormula
from vista import Vista
class Controlador:
    def __init__(self):
        pass

    def pasarDatos(self,datos):
        datosPersona=json.dumps(datos)
        with open("baseDatos.txt", "w") as archivo:
            json.dump(datosPersona,archivo)


#objModelo=modeloFormula()
objControlador=Controlador()
objVIsta=Vista(objControlador)
objVIsta.crearVentana()