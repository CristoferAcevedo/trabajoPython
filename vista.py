import tkinter as ventana

class Vista:
      def __init__(self):
            pass
      
      def crearVentana(self,Ventana):
            botonCrear=ventana.Button(text="crear texto",command=self.crearTexto)
            botonCrear.pack(padx=10,pady=10)
            botonModificar=ventana.Button(text="modificar texto", command=self.modificarTexto)
            botonModificar.pack(padx=10,pady=10)
            botonMostrar=ventana.Button(text="mostrar texto", command=self.mostrarTexto)
            botonMostrar.pack(padx=10,pady=10)
            botonEliminar=ventana.Button(text="eliminar texto", command=self.eliminarTexto)
            botonEliminar.pack(padx=10,pady=10)
            botonSalir=ventana.Button(text="salir",command=lambda:self.salir(Ventana))
            botonSalir.pack(padx=10,pady=10)

      def crearTexto(self):
            self.ventanaCrear=ventana.Toplevel()
            self.ventanaCrear.title("creacion de texto")
            self.ventanaCrear.minsize(width=300,height=300)
            self.ventanaCrear.config(background="#40cfff")
            self.contenedor=ventana.Frame(self.ventanaCrear,bg="#40cfff")
            self.contenedor.pack(padx=20,pady=20)
            self.nombre=ventana.StringVar()
            self.apellido=ventana.StringVar()
            self.edad=ventana.IntVar()
            self.correo=ventana.StringVar()
            self.genero=ventana.StringVar()
            generos=[("masculino","masculino"),("femenino","femenino"),("otro","otro")]
            self.labelNombre=ventana.Label(self.contenedor,text="ingrese el nombre")
            self.labelNombre.grid(column=1,row=1)
            self.entryNombre=ventana.Entry(self.contenedor,textvariable=self.nombre)
            self.entryNombre.grid(column=2,row=1)
            self.labelApellido=ventana.Label(self.contenedor,text="ingrese el apellido")
            self.labelApellido.grid(column=1,row=2)
            self.entryApellido=ventana.Entry(self.contenedor,textvariable=self.apellido)
            self.entryApellido.grid(column=2,row=2)
            self.labelEdad=ventana.Label(self.contenedor,text="ingrese su edad")
            self.labelEdad.grid(column=1,row=3)
            self.entryEdad=ventana.Entry(self.contenedor,textvariable=self.edad)
            self.entryEdad.grid(column=2,row=3)
            self.labelCorreo=ventana.Label(self.contenedor,text="ingrese su correo")
            self.labelCorreo.grid(column=1,row=4)
            self.entryCorreo=ventana.Entry(self.contenedor,textvariable=self.correo)
            self.entryCorreo.grid(column=2,row=4)
            self.labelGenero=ventana.Label(self.contenedor,text="eliga el genero")
            self.labelGenero.grid(column=1,row=5)
            for texto, valor in generos:
                  ventana.Radiobutton(self.contenedor, text=texto, variable=self.genero, value=valor).grid(column=2, row=generos.index((texto, valor))+5)
            self.botonRegistrar=ventana.Button(self.contenedor,text="registrar datos")
            self.botonRegistrar.grid(column=2,row=9)

      def modificarTexto(self):
            print("hola")

      def mostrarTexto(self):
            print("loas")

      def eliminarTexto(self):
            print("Qwe")

      def salir(self,Ventana):
            Ventana.destroy()
            
Ventana=ventana.Tk()
Ventana.title("menu")
Ventana.minsize(width=300, height=300)
Ventana.config(background="#40cfff")
vista=Vista()
vista.crearVentana(Ventana)
Ventana.mainloop()