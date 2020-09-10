from tkinter import *
import os

# clase para ventana de confirmacion para cambiar bloque de nombres de archivos
class Ventana:

    def __init__(self, root, _ruta_app):
        # crear ventana de aviso
        self.root = root
        self.root.title('Confirmar Acción')
        self.root.config(bg="black")
        self.root.geometry("350x115")  # tamaño y posicion
        self.root.resizable(width=FALSE, height=FALSE)  # no redimensiona
        self.root.attributes("-topmost", True)  # colocar al frente la ventana
        # titulo central
        self.etiqueta = Label(self.root, text="Confirmar Acción", font=("arial", 14), bg="gray", fg="white")
        self.etiqueta.pack(padx=0, pady=0, fill=BOTH, expand=1)
        # descripcion
        self.texto = 'None...'
        self.descripcion = Label(self.root, text=self.texto, justify=CENTER,
                                 font=("arial", 12), bg="black", fg="white")
        self.descripcion.pack(padx=0, pady=5, fill=BOTH, ipadx=5, ipady=5)
        # botones
        self.btn_si = Button(self.root, text="Aplicar", width=4, font=("arial", 12))
        self.btn_si.pack(side=LEFT, fill=BOTH, expand=1)
        self.btn_no = Button(self.root, text="No", width=4, font=("arial", 12))
        self.btn_no.pack(side=LEFT, fill=BOTH, expand=1)

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
