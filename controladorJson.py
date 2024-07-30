import json
from modelotrabajoAC import modeloFormula
from vista import Vista
class Controlador:
    def __init__(self,objModelo):
        self.objModelo=objModelo

    def pasarDatos(self,datos):
        datosPersona=json.dumps(datos)
        self.objModelo.crearArchivo(datosPersona)

    def enviarMostrar(self):
        aux=self.objModelo.leerArchivo()
        return aux

    def enviarModificar(self,datos2):
        datosPersona2=json.dumps(datos2)
        self.objModelo.modificarArchivo(datosPersona2)

    def enviarEliminar(self):
        self.objModelo.eliminarArchivo()



objModelo=modeloFormula()
objControlador=Controlador(objModelo)
objVIsta=Vista(objControlador)
objVIsta.crearVentana()
