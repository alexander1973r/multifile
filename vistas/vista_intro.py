from tkinter import *
from PIL import Image, ImageTk  # se usa para ajustar imagen
import os


# clase para ventana de confirmacion para cambiar bloque de nombres de archivos
class Ventana:

    def __init__(self, root, ruta_app):
        # crear ventana de aviso
        self.root = root
        self.root.title('Multifile Ver 1.0')
        self.root.config(bg="black")
        self.root.geometry("382x176")  # tamaño y posicion
        self.root.resizable(width=FALSE, height=FALSE)  # no redimensiona
        self.root.attributes("-topmost", True)  # colocar al frente la ventana
        # imagen r"../vistas/imagen/LOGOprogramMultifile.jpg"  <-- ruta cuando se llama desde la vista
        self.ruta_icono = os.path.join(ruta_app, 'vistas', 'imagen',
                                       'LOGOprogramMultifile.jpg')  # ruta donde esta el app + icono
        self.img5 = Image.open(self.ruta_icono)  # se usa otra variable
        self.img5 = self.img5.resize((382, 177), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img5)  # convert to PhotoImage
        self.etiqueta = Label(self.root, image=self.img)
        # self.etiqueta.pack(pady=2, padx=2)
        self.etiqueta.place(x=0,y=0)

        # Contador de tiempo
        self.etiqueta_contador = Label(self.root, text="",
                                  width=2, fg="black",
                                  font=("arial", "16"))
        self.etiqueta_contador.place(x=345,y=140)


    # Metodo para cerrar ventana
    def cerrar_vent(self):
        self.root.destroy()

    # Metodo para destruir ventana al cerrarla
    def _onDestroy(self):
        self.root.destroy()

# -----------------------
# probador de ventana
# root = Tk()
# ruta = os.getcwd()  # ruta actual
# ruta  = os.path.join(ruta, '..')
# gui_ppal = Ventana(root, ruta)
# root.mainloop()

