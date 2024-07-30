import json
class modeloFormula:
    def __init__(self):
        self.listaDatos=[]
    
    def crearArchivo(self,datoTexto):
        self.listaDatos.append(datoTexto)
        datos=json.dumps(self.listaDatos)
        with open("baseDatos.txt","w") as archivoTexto:
            archivoTexto.write("")
        archivoTexto.close()
        with open("baseDatos.txt", "a") as archivoTexto:
            archivoTexto.write(datos)
        archivoTexto.close()

    def leerArchivo(datotexto):
        with open("baseDatos.txt","r") as archivo:
            datoContenido=archivo.read()
            print(datoContenido)
        archivo.close()
        return datoContenido
            
    def modificarArchivo(self,datoTexto2):
        with open("baseDatos.txt","w") as archivoTexto:
            archivoTexto.write(datoTexto2)
            print(archivoTexto)
        archivoTexto.close()

    def eliminarArchivo(self):
        with open("baseDatos.txt", "w") as archivo:
            archivo.write("")
        archivo.close()
