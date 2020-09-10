from tkinter import *  # para tkinter y widgets
from tkinter import ttk  # para el treeview
from PIL import Image, ImageTk  # para ajustar imagen
import os


# creacion de ventana
class Ventana:

    def __init__(self, root, ruta_app):
        self.ruta_app = ruta_app  # ruta de applicacion
        self.valor = 0
        # ventana principal
        self.root = root
        self.root.title("MultiFile V 1.0")
        self.root.geometry("600x400")  # tamaño y posicion
        self.root.minsize(width=600, height=490)
        self.root.configure(background='#272829')

        # cajon de botones superior 1
        self.frame_a = Frame(root)
        self.frame_a.pack(anchor=NW, fill=BOTH)

        # todos los archivos
        self.ruta_icono = os.path.join(ruta_app, 'vistas', 'iconos',
                                       'todoslosarchivos.png')  # ruta donde esta el app + icono
        self.img2 = Image.open(self.ruta_icono)  # se usa otra variable
        self.img2 = self.img2.resize((32, 32), Image.ANTIALIAS)  # The (32 32) es (altura, ancho)
        self.img2 = ImageTk.PhotoImage(self.img2)  # convert to PhotoImage
        self.btn_allFile = Button(self.frame_a, bg="#b8bcbd", image=self.img2)
        self.btn_allFile.pack(anchor=NW, side=LEFT)
        # un archivo
        self.ruta_icono = os.path.join(ruta_app, 'vistas', 'iconos',
                                       'unarchivo.png')  # ruta donde esta el app + icono
        self.img = Image.open(self.ruta_icono)  # PIL carga la imagen
        self.img = self.img.resize((32, 32), Image.ANTIALIAS)  # The (32 32) es (altura, ancho)
        self.img = ImageTk.PhotoImage(self.img)  # convert to PhotoImage
        self.btn_unFile = Button(self.frame_a, bg="#b8bcbd", image=self.img)
        self.btn_unFile.pack(anchor=NW, side=LEFT)
        # borrar
        self.ruta_icono = os.path.join(ruta_app, 'vistas', 'iconos',
                                       'borrar.png')  # ruta donde esta el app + icono
        self.img3 = Image.open(self.ruta_icono)  # se usa otra variable
        self.img3 = self.img3.resize((32, 32), Image.ANTIALIAS)  # The (32 32) es (altura, ancho)
        self.img3 = ImageTk.PhotoImage(self.img3)  # convert to PhotoImage
        self.btn_del = Button(self.frame_a, bg="#b8bcbd", image=self.img3)
        self.btn_del.pack(anchor=NW, side=LEFT)
        # --------------------------------------------------------
        # icono de menu (MENU)
        self.ruta_icono = os.path.join(ruta_app, 'vistas', 'iconos',
                                       'menu.png')  # ruta donde esta el app + icono
        self.img4 = Image.open(self.ruta_icono)  # se usa otra variable
        self.img4 = self.img4.resize((32, 32), Image.ANTIALIAS)  # The (32 32) es (altura, ancho)
        self.img4 = ImageTk.PhotoImage(self.img4)  # convert to PhotoImage
        # submenus
        self.btn_menu = Menubutton(self.frame_a, bg="#b8bcbd", image=self.img4)  # crea el botom menu
        self.btn_menu.pack(anchor=NW, side=RIGHT)
        self.submenu1 = Menu(self.btn_menu, tearoff=0)
        self.btn_menu.config(menu=self.submenu1)  # a quien pertenece el submenu
        self.submenu1.add_command(label="Agregar Ruta")
        self.submenu1.add_command(label="Quitar Ruta")
        self.submenu1.add_separator()
        self.submenu1.add_command(label="Renombrar un archivo")
        self.submenu1.add_command(label="Renombrar Grupo de archivos")
        self.submenu1.add_command(label="Borrar un Archivo")
        self.submenu1.add_separator()
        self.submenu1.add_command(label="Acerca ...")
        self.submenu1.add_command(label="Salir")

        # cajon de botones superior 2 combobox
        self.frame_b = Frame(root)
        self.frame_b.pack(anchor=NW, fill=BOTH)
        # combobox
        self.n = StringVar()
        self.combobox_widget = ttk.Combobox(self.frame_b, width=30,
                                            textvariable=self.n)
        self.combobox_widget['values'] = []
        self.combobox_widget.set('')  # limpiar campo combobox
        self.combobox_widget.pack(padx=5, side=LEFT, fill=X, expand=1)  # poner en la geometria
        # icono ir a ruta path disco duro
        self.ruta_icono = os.path.join(ruta_app, 'vistas', 'iconos',
                                       'ir.png')  # ruta donde esta el app + icono
        self.img5 = Image.open(self.ruta_icono)  # se usa otra variable
        self.img5 = self.img5.resize((24, 24), Image.ANTIALIAS)  # The (16 16) es (altura, ancho)
        self.img5 = ImageTk.PhotoImage(self.img5)  # convert to PhotoImage
        self.btn_irRuta = Button(self.frame_b, bg="#b8bcbd", image=self.img5)
        self.btn_irRuta.pack(anchor=NW, side=RIGHT, padx=2, pady=2)

        # frame para contener el Treeview (medio)
        self.frame_c = Frame(root)
        self.frame_c.pack(fill=BOTH, expand=1)  # se ajusta a toda la ventana y llena x/y

        # creando widget de tabla para vista (no se usa modo show=heading)
        self.tree = ttk.Treeview(self.frame_c, height=18)
        self.tree["columns"] = ("Nombre", "Tipo", "Size")  # columnas creadas
        self.tree.heading('#0', text="Nombre")
        self.tree.heading('#1', text="Tipo")
        self.tree.heading('#2', text="Size")
        # creando columnas de la tabla treeview
        self.tree.column("#0", anchor='w', minwidth=398, stretch=YES)
        self.tree.column("#1", width=60, minwidth=60, anchor='e', stretch=NO)  # forzamos el tamño
        self.tree.column("#2", width=120, anchor='e', stretch=NO)
        # Scroll Y
        self.treeYScroll = Scrollbar(self.frame_c, orient=VERTICAL)
        self.treeYScroll.configure(command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.treeYScroll.set)
        self.treeYScroll.pack(side=RIGHT, fill=Y)
        # pack (el orden para colocar asignar los widgets es importante para mostrarlo
        self.tree.pack(fill=BOTH, expand=1)

        # set ttk theme to "clam" which support the fieldbackground option
        self.style = ttk.Style(root)
        self.style.theme_use("clam")
        self.style.configure("Treeview", background="black",
                             fieldbackground="black", foreground="white", font=("arial", "11"))
        # ---------------------------------------------------------------------
        # cajon de resultado pie de controles
        self.frame_d = Frame(root, bg="black")
        self.frame_d.pack(anchor=NW, fill=BOTH)

        # notice
        self.label_notice = Label(self.frame_d, text="",
                                  width=14, bg="black", fg="yellow",
                                  font=("arial", "10"))
        self.label_notice.pack(anchor=NW, pady=5, padx=5, side=LEFT)
        # LABEL KB
        self.label_nombre_kb = Label(self.frame_d, text="",
                                     width=14, bg="black", fg="grey",
                                     font=("arial", "10"))
        self.label_nombre_kb.pack(anchor=NW, pady=5, padx=5, side=RIGHT)
        label_titulo_kb = Label(self.frame_d, text="Kbytes:",  # label Bytes
                                bg="black", fg="white",
                                font=("arial", "10"))
        label_titulo_kb.pack(anchor=NW, pady=5, padx=5, side=RIGHT)

        # LABEL DIR
        self.label_num_dirs = Label(self.frame_d, text="",
                                    width=6, bg="black", fg="grey",
                                    font=("arial", "10"))
        self.label_num_dirs.pack(anchor=NW, pady=5, padx=5, side=RIGHT)
        label_titulo_cant_dir = Label(self.frame_d, text="Dirs:",  # label Dirs
                                      bg="black", fg="white",
                                      font=("arial", "10"))
        label_titulo_cant_dir.pack(anchor=NW, pady=5, padx=5, side=RIGHT)

        self.label_num_files = Label(self.frame_d, text="",
                                     width=6, bg="black", fg="grey",
                                     font=("arial", "10"))
        self.label_num_files.pack(anchor=NW, pady=5, padx=5, side=RIGHT)
        label_titulo_cant_files = Label(self.frame_d, text="Files:",  # label Files
                                        bg="black", fg="white",
                                        font=("arial", "10"))
        label_titulo_cant_files.pack(anchor=NW, pady=5, padx=5, side=RIGHT)

        # ------------------------
        # carga de iconos de tabla res 18x18px
        self.ruta_icono = os.path.join(ruta_app, 'vistas', 'iconos',
                                       'file18x18px.png')  # ruta donde esta el app + icono
        self.icono_file = PhotoImage(file=self.ruta_icono)
        self.ruta_icono = os.path.join(ruta_app, 'vistas', 'iconos',
                                       'folder18x18px.png')  # ruta donde esta el app + icono
        self.icono_folder = PhotoImage(file=self.ruta_icono)

    # ---------------------------------------------------

    # Se crea este metodo para resolver el colocar imagenes y contenido en el tree
    # al tratar de cargar imagenes desde afuera por una funcion  externa no son generada
    def insertar(self, name, tipo, size, i):
        if tipo == 'File':
            self.tree.insert('', 'end', text=name, image=self.icono_file,
                             value=(tipo, size), tags=(i,))
        elif tipo == '[DIR]':
            self.tree.insert('', 'end', text=name, image=self.icono_folder,
                             value=(tipo, size), tags=(i,))
        else:
            self.tree.insert('', 'end', text=name,
                             value=('', size), tags=(i,))

# -----------------------
# probador de ventana
# root = Tk()
# ruta = os.getcwd()  # ruta actual
# ruta  = os.path.join(ruta, '..')
# gui_ppal = Ventana(root, ruta)
# root.mainloop()
