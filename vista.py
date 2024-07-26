import tkinter as ventana

class Vista:
      def __init__(self):
            pass
      
      def crearVentana(self):
            self.ventana=ventana.Tk()
            self.ventana.title("Json")
            self.ventana.config(background="gray")
            self.ventana.geometry("300x300")
            self.ventana.mainloop()
            crearTexto=ventana.Label(text="ingrese el titulo del texto")
            crearTexto.pack()
            
            
vista=Vista()
vista.crearVentana()