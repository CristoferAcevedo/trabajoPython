class modeloFormula:
    def __init__(self):
        pass
    
    def crearArchivo(datoTexto):
        nombreArchivo=str(input("Escriba el nombre del archivo: "))
        nombreArchivo=nombreArchivo+".Txt"
        with open(nombreArchivo,"w") as archivoTexto:
            archivoTexto.write(datoTexto)
            mensaje="documento creado.."
        archivoTexto.close()
        return mensaje

    def leerArchivo():
        with open("cristofer.txt","r") as archivo:
            datoContenido=archivo.read()
            print(datoContenido)
            archivo.close()
            
    def leerLinea():
        with open("cristofer.txt","r") as archivo:
            datoContenido=archivo.readline()
            print(datoContenido)
            archivo.close()
            
    def leerLineas():
        with open("cristofer.txt","r") as archivo:
            datoContenido=archivo.readlines()
            print(datoContenido)
            print("cantidad de renglones: ",len(datoContenido))
            archivo.close()
            
    def escribeCadenas():
        listaDatos=["primera linea.\n","segunda linea\n","tercera linea\n"]
        with open("cristofer.txt","w") as archivo:
            archivo.writelines(listaDatos)
            print("cantidad de renglones: ",len(listaDatos))
            archivo.close()
    
    
    aux=hacerTexto()
    crearArchivo(aux)
    leerArchivo()
    leerLinea()
    leerLineas()
    escribeCadenas()
    
        
    def crearArchivo(self,datoTexto):
        nombreArchivo=str(input("Escriba el nombre del archivo: "))
        nombreArchivo=nombreArchivo+".Txt"
        with open(nombreArchivo,"w") as archivoTexto:
            archivoTexto.write(datoTexto)
            mensaje="documento creado.."
        archivoTexto.close()
        return mensaje

    def leerArchivo():
        with open("cristofer.txt","r") as archivo:
            datoContenido=archivo.read()
            print(datoContenido)
            archivo.close()
            
    def leerLinea():
        with open("cristofer.txt","r") as archivo:
            datoContenido=archivo.readline()
            print(datoContenido)
            archivo.close()
            
    def leerLineas():
        with open("cristofer.txt","r") as archivo:
            datoContenido=archivo.readlines()
            print(datoContenido)
            print("cantidad de renglones: ",len(datoContenido))
            archivo.close()
            
    def escribeCadenas():
        listaDatos=["primera linea.\n","segunda linea\n","tercera linea\n"]
        with open("cristofer.txt","w") as archivo:
            archivo.writelines(listaDatos)
            print("cantidad de renglones: ",len(listaDatos))
            archivo.close()


    aux=hacerTexto()
    crearArchivo(aux)
    leerArchivo()
    leerLinea()
    leerLineas()
    escribeCadenas()
