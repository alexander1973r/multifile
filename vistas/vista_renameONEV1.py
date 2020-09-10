from tkinter import *  # para tkinter y widgets


# ventana para cambiar el nombre de un solo archivo
class Ventana:

    def __init__(self, root):
        self.existe = True
        # crear ventana para cambiar un solo nombre
        self.root = root
        self.nombre_archivo_viejo = 'demo'  # atributo del nombre viejo del archivo
        self.root.title("Renombrar [UNO]")
        self.root.geometry("450x80")  # tamaño y posicion
        self.root.minsize(width=450, height=80)
        self.root.configure(background='#272829')
        self.root.resizable(height=FALSE)  # no redimensiona
        self.root.attributes("-topmost", True)  # colocar al frente la ventana
        # captura evento de cerrar ventana y lo direcciona a una funcion
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_vent)

        # # Campo de cambiar nombre
        self.frame_01 = Frame(self.root, bg="black")  # frame para el label y Entry
        self.frame_01.pack(anchor=NW, fill=BOTH)
        self.label_01 = Label(self.frame_01, text="Nuevo nombre:",
                              fg="white", bg="black", font=("arial", 12))  # label identifica Campo de Entrada
        self.label_01.pack(anchor=NW, side=LEFT, pady=5)
        self.nombre_archivo = StringVar()  # variable de entrada string
        self.campo_nombre_archivo = Entry(self.frame_01, font=("arial", 12),
                                          textvariable=self.nombre_archivo)  # Campo de entrada
        self.campo_nombre_archivo.pack(anchor=E, side=LEFT, pady=5, padx=5, fill=X, expand=1)

        # botones
        self.frame_02 = Frame(self.root, bg="black")  # frame para el label y Entry
        self.frame_02.pack(anchor=NW, fill=BOTH)
        self.btn_si = Button(self.frame_02, text="Cambiar", font=("arial", 12))
        self.btn_si.pack(side=LEFT, fill=BOTH, expand=1, pady=5, padx=5)
        self.btn_no = Button(self.frame_02, text="Salir", font=("arial", 12))
        self.btn_no.pack(side=LEFT, fill=BOTH, expand=1, pady=5, padx=5)

        # eventos (Capturar el cierre de la ventana)
        self.root.bind("<Destroy>", self._onDestroy)

    # Metodo para cerrar ventana
    def cerrar_vent(self):
        self.existe = False
        del self.existe
        self.root.destroy()

    # Metodo para destruir ventana al cerrarla
    def _onDestroy(self, e):
        self.existe = False
        del self.existe
        self.root.destroy()


# -----------------------
# cargar ventana principal
# raiz = Tk()
# gui_ppal = Ventana(raiz)
# raiz.mainloop()
