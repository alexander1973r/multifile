from tkinter import *  # para tkinter y widgets


# ventana para cambiar el nombre de un solo archivo GRUPALES
class Ventana:

    def __init__(self, root):
        self.existe = True
        # crear ventana para cambiar un solo nombre
        self.root = root
        self.root.title("Renombrar [GRUPO]")
        self.root.geometry("450x280")  # tamaño y posicion
        self.root.minsize(width=450, height=280)
        self.root.configure(background='#272829')
        self.root.resizable(height=FALSE, width=FALSE)  # no redimensiona
        self.root.attributes("-topmost", True)  # colocar al frente la ventana

        # CAPTURAR evento de cerrar ventana y lo direcciona a una funcion
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_vent)

        # # Campo a buscar nombre
        self.frame_01 = Frame(self.root, bg="black")  # frame para el label y Entry
        self.frame_01.pack(anchor=NW, fill=BOTH)
        self.label_01 = Label(self.frame_01, text="Buscar palabra:",
                              fg="white", bg="black", font=("arial", 12))  # label identifica Campo de Entrada
        self.label_01.pack(anchor=NW, side=LEFT, pady=5)
        self.archivo_buscar = StringVar()  # variable de entrada string
        self.campo_nombre_buscar = Entry(self.frame_01, font=("arial", 12),
                                         textvariable=self.archivo_buscar)  # Campo de entrada
        self.campo_nombre_buscar.pack(anchor=E, side=LEFT, pady=5, padx=5, fill=X, expand=1)

        # # Campo a cambiar nombre
        self.frame_03 = Frame(self.root, bg="black")  # frame para el label y Entry
        self.frame_03.pack(anchor=NW, fill=BOTH)
        self.label_03 = Label(self.frame_03, text="Cambiar por:",
                              fg="white", bg="black", font=("arial", 12))  # label identifica Campo de Entrada
        self.label_03.pack(anchor=NW, side=LEFT, pady=5)
        self.archivo_cambiar = StringVar()  # variable de entrada string
        self.campo_nombre_cambiar = Entry(self.frame_03, font=("arial", 12),
                                          textvariable=self.archivo_cambiar)  # Campo de entrada
        self.campo_nombre_cambiar.pack(anchor=E, side=LEFT, pady=5, padx=5, fill=X, expand=1)

        # botones
        self.frame_02 = Frame(self.root, bg="black")  # frame para el label y Entry
        self.frame_02.pack(anchor=NW, fill=BOTH)
        self.btn_si = Button(self.frame_02, text="Buscar Archivos", font=("arial", 12))
        self.btn_si.pack(side=LEFT, fill=BOTH, expand=1, pady=5, padx=5)

        # titulo central
        self.etiqueta = Label(self.root, text="Confirmar Acción", font=("arial", 14), bg="gray", fg="white")
        self.etiqueta.pack(padx=0, pady=0, fill=BOTH, expand=1)
        # descripcion
        self.texto = 'None...'
        self.descripcion = Label(self.root, text=self.texto, justify=CENTER,
                                 font=("arial", 12), bg="black", fg="white")
        self.descripcion.pack(padx=0, pady=5, fill=BOTH, ipadx=5, ipady=5)

        # botones
        self.btn_aplicar = Button(self.root, text="Aplicar", width=4, font=("arial", 12))
        self.btn_aplicar.pack(side=LEFT, fill=BOTH, expand=1)
        self.btn_no_salir = Button(self.root, text="No", width=4, font=("arial", 12))
        self.btn_no_salir.pack(side=LEFT, fill=BOTH, expand=1)

    # Metodo para cerrar ventana
    def cerrar_vent(self):
        self.existe = False
        del self.existe
        self.root.destroy()

    # Metodo para destruir ventana al cerrarla
    def _onDestroy(self):
        self.existe = False
        del self.existe
        self.root.destroy()


# -----------------------
# probador de ventana
# raiz = Tk()
# gui_ppal = Ventana(raiz)
# raiz.mainloop()
