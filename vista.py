import tkinter as ventana
from tkinter import messagebox
import json
class Vista:
    def __init__(self,objControlador):
        self.objControlador=objControlador

    def crearVentana(self):
        self.Ventana=ventana.Tk()
        self.Ventana.title("menu")
        self.Ventana.minsize(width=300, height=300)
        self.Ventana.config(background="#40cfff")
        botonCrear=ventana.Button(text="crear texto",command=self.crearTexto)
        botonCrear.pack(padx=10,pady=10)
        botonCrear.config(cursor="hand2")
        botonModificar=ventana.Button(text="modificar texto", command=self.modificarTexto)
        botonModificar.pack(padx=10,pady=10)
        botonModificar.config(cursor="hand2")
        botonMostrar=ventana.Button(text="mostrar texto", command=self.mostrarTexto)
        botonMostrar.pack(padx=10,pady=10)
        botonMostrar.config(cursor="hand2")
        botonEliminar=ventana.Button(text="eliminar texto", command=self.eliminarTexto)
        botonEliminar.pack(padx=10,pady=10)
        botonEliminar.config(cursor="hand2")
        botonSalir=ventana.Button(text="salir",command=lambda:self.salir(self.Ventana))
        botonSalir.pack(padx=10,pady=10)
        botonSalir.config(cursor="hand2")

        self.Ventana.mainloop()

    def crearTexto(self):
        self.ventanaCrear=ventana.Toplevel()
        self.ventanaCrear.title("creacion de texto")
        self.ventanaCrear.minsize(width=300,height=300)
        self.ventanaCrear.config(background="#40cfff")
        self.contenedor=ventana.Frame(self.ventanaCrear,bg="#40cfff")
        self.contenedor.pack(padx=20,pady=20)
        self.documentoId=ventana.StringVar()
        self.numeroDocumento=ventana.StringVar()
        self.nombre=ventana.StringVar()
        self.apellido=ventana.StringVar()
        self.edad=ventana.IntVar()
        self.correo=ventana.StringVar()
        self.genero=ventana.StringVar()
        generos=[("masculino","masculino"),("femenino","femenino"),("otro","otro")]
        documentos=[("cedula de identidad","cedula de identidad"),("tarjeta de identidad","tarjeta de identidad")]
        self.labelDocumentoId=ventana.Label(self.contenedor,text="elija el tipo de documento de identidad")
        self.labelDocumentoId.grid(column=1,row=1)
        for texto, valor in documentos:
              ventana.Radiobutton(self.contenedor, text=texto, variable=self.documentoId, value=valor).grid(column=2, row=documentos.index((texto, valor))+1)
        self.labelNumeroDocumento=ventana.Label(self.contenedor,text="ingrese el numero de documento")
        self.labelNumeroDocumento.grid(column=1,row=3)
        self.entryNumeroDocumento=ventana.Entry(self.contenedor,textvariable=self.numeroDocumento)
        self.entryNumeroDocumento.grid(column=2,row=3)
        self.labelNombre=ventana.Label(self.contenedor,text="ingrese el nombre")
        self.labelNombre.grid(column=1,row=4)
        self.entryNombre=ventana.Entry(self.contenedor,textvariable=self.nombre)
        self.entryNombre.grid(column=2,row=4)
        self.labelApellido=ventana.Label(self.contenedor,text="ingrese el apellido")
        self.labelApellido.grid(column=1,row=5)
        self.entryApellido=ventana.Entry(self.contenedor,textvariable=self.apellido)
        self.entryApellido.grid(column=2,row=5)
        self.labelEdad=ventana.Label(self.contenedor,text="ingrese su edad")
        self.labelEdad.grid(column=1,row=6)
        self.entryEdad=ventana.Entry(self.contenedor,textvariable=self.edad)
        self.entryEdad.grid(column=2,row=6)
        self.labelCorreo=ventana.Label(self.contenedor,text="ingrese su correo")
        self.labelCorreo.grid(column=1,row=7)
        self.entryCorreo=ventana.Entry(self.contenedor,textvariable=self.correo)
        self.entryCorreo.grid(column=2,row=7)
        self.labelGenero=ventana.Label(self.contenedor,text="eliga el genero")
        self.labelGenero.grid(column=1,row=8)
        for texto, valor in generos:
              ventana.Radiobutton(self.contenedor, text=texto, variable=self.genero, value=valor).grid(column=2, row=generos.index((texto, valor))+8)
        self.botonRegistrar=ventana.Button(self.contenedor,text="registrar datos",command=lambda:self.enviarDatos(self.numeroDocumento,self.documentoId,self.nombre,self.apellido,self.edad,self.correo,self.genero))
        self.botonRegistrar.grid(column=2,row=15)
        self.botonRegistrar.config(cursor="hand2")

    def enviarDatos(self,datoNumeroDocumento,datoDocumentoId,datoNombre,datoApellido,datoEdad,datoCorreo,datoGenero):
        self.ventanaCrear.destroy()
        messagebox.showinfo("creado","texto creado con exito")
        numeroDocumento=datoDocumentoId.get()
        documentoID=datoNumeroDocumento.get()
        nombre=datoNombre.get()
        apellido=datoApellido.get()
        edad=datoEdad.get()
        correo=datoCorreo.get()
        genero=datoGenero.get()
        self.datos={
            "tipo de documento":numeroDocumento,
            "documento de identidad":documentoID,
            "nombre":nombre,"apellido":apellido,
            "edad":edad,
            "correo":correo,
            "genero":genero
            }
        self.objControlador.pasarDatos(self.datos)


    def modificarTexto(self):
        self.ventanaModificar=ventana.Toplevel()
        self.ventanaModificar.title("modificacion de texto")
        self.ventanaModificar.minsize(width=300,height=300)
        self.ventanaModificar.config(background="#40cfff")
        self.contenedor2=ventana.Frame(self.ventanaModificar,bg="#40cfff")
        self.contenedor2.pack(padx=20,pady=20)
        self.documentoId=ventana.StringVar()
        self.numeroDocumento=ventana.StringVar()
        self.nombre=ventana.StringVar()
        self.apellido=ventana.StringVar()
        self.edad=ventana.IntVar()
        self.correo=ventana.StringVar()
        self.genero=ventana.StringVar()
        generos=[("masculino","masculino"),("femenino","femenino"),("otro","otro")]
        documentos=[("cedula de identidad","cedula de identidad"),("tarjeta de identidad","tarjeta de identidad")]
        self.labelDocumentoId=ventana.Label(self.contenedor2,text="elija el tipo de documento de identidad")
        self.labelDocumentoId.grid(column=1,row=1)
        for texto, valor in documentos:
              ventana.Radiobutton(self.contenedor2, text=texto, variable=self.documentoId, value=valor).grid(column=2, row=documentos.index((texto, valor))+1)
        self.labelNumeroDocumento=ventana.Label(self.contenedor2,text="ingrese el numero de documento")
        self.labelNumeroDocumento.grid(column=1,row=3)
        self.entryNumeroDocumento=ventana.Entry(self.contenedor2,textvariable=self.numeroDocumento)
        self.entryNumeroDocumento.grid(column=2,row=3)
        self.labelNombre=ventana.Label(self.contenedor2,text="ingrese el nombre")
        self.labelNombre.grid(column=1,row=4)
        self.entryNombre=ventana.Entry(self.contenedor2,textvariable=self.nombre)
        self.entryNombre.grid(column=2,row=4)
        self.labelApellido=ventana.Label(self.contenedor2,text="ingrese el apellido")
        self.labelApellido.grid(column=1,row=5)
        self.entryApellido=ventana.Entry(self.contenedor2,textvariable=self.apellido)
        self.entryApellido.grid(column=2,row=5)
        self.labelEdad=ventana.Label(self.contenedor2,text="ingrese su edad")
        self.labelEdad.grid(column=1,row=6)
        self.entryEdad=ventana.Entry(self.contenedor2,textvariable=self.edad)
        self.entryEdad.grid(column=2,row=6)
        self.labelCorreo=ventana.Label(self.contenedor2,text="ingrese su correo")
        self.labelCorreo.grid(column=1,row=7)
        self.entryCorreo=ventana.Entry(self.contenedor2,textvariable=self.correo)
        self.entryCorreo.grid(column=2,row=7)
        self.labelGenero=ventana.Label(self.contenedor2,text="eliga el genero")
        self.labelGenero.grid(column=1,row=8)
        for texto, valor in generos:
              ventana.Radiobutton(self.contenedor2, text=texto, variable=self.genero, value=valor).grid(column=2, row=generos.index((texto, valor))+8)
        self.botonModificar=ventana.Button(self.contenedor2,text="modificar datos",command=lambda:self.enviarDatosModificar(self.numeroDocumento,self.documentoId,self.nombre,self.apellido,self.edad,self.correo,self.genero))
        self.botonModificar.grid(column=2,row=15)
        self.botonModificar.config(cursor="hand2")

    def enviarDatosModificar(self,datoNumeroDocumento,datoDocumentoId,datoNombre,datoApellido,datoEdad,datoCorreo,datoGenero):
        self.ventanaModificar.destroy()
        messagebox.showinfo("modificar","texto modificado con exito")
        numeroDocumento=datoDocumentoId.get()
        documentoID=datoNumeroDocumento.get()
        nombre=datoNombre.get()
        apellido=datoApellido.get()
        edad=datoEdad.get()
        correo=datoCorreo.get()
        genero=datoGenero.get()
        self.datosModificados={
            "tipo de documento":numeroDocumento,
            "documento de identidad":documentoID,
            "nombre":nombre,
            "apellido":apellido,
            "edad":edad,
            "correo":correo,
            "genero":genero
            }
        self.objControlador.enviarModificar(self.datosModificados)

    def mostrarTexto(self):
        aux=self.objControlador.enviarMostrar()
        datos=json.loads(aux)
        messagebox.showinfo("Datos del Archivo", datos)

    def eliminarTexto(self):
        self.objControlador.enviarEliminar()
        messagebox.showinfo("eliminado","texto eliminado con exito")

    def salir(self,Ventana):
        Ventana.destroy()
            
