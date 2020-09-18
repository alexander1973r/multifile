from tkinter import *
from tkinter import messagebox as mb  # submodulo de messegebox
import os

# -----------------------------------
# # VISTAS
from vistas import vista_principalV1 as Ppal
# -----------------------------------
# CONTROLADOR
from controlador import control_borrar_un_archivo as Borrar
from controlador import control_renombrar_un_archivo as RenUno
from controlador import control_renombrar_grupo_archivo as RenGrupo
from controlador import control_acerca as Acerca
# -----------------------------------
# MODELOS
from modelos import funcion_rutasV1 as Rutas


# -----------------------------------
# FUNCIONES
# -----------------------------------

# FUNCION: para cargar contenido de la tabla
def cargar_tabla(lista_directorio, gui_ppal):
    if lista_directorio is not None:
        gui_ppal.tree.delete(*gui_ppal.tree.get_children())  # borrar todos los items
        lista_directorio.insert(0, "..")  # insertar: .. para bajar nivel directorio
        tl_files = 0
        tl_dirs = 0
        tl_size = 0
        # llenar la tabla
        for i, archivo in enumerate(lista_directorio):
            size = os.path.getsize(archivo)
            es_file = os.path.isfile(archivo)
            es_dir = os.path.isdir(archivo)
            tl_size += size  # totalizar archivos
            # identificar el tipo
            if es_file:
                tipo = 'File'
                tl_files += 1
                size = f"{size:,}"
            elif es_dir:
                tipo = "[DIR]"
                size = ''
                tl_dirs += 1
            else:
                tipo = "?"

            gui_ppal.insertar(archivo, tipo, size, i)  # cargar filas en la tabla
            # Resaltar el color para directorios
            if es_dir:
                gui_ppal.tree.tag_configure(i, foreground="blue",
                                            background='black')  # id para cada item de archivo
            else:
                gui_ppal.tree.tag_configure(i, foreground="white",
                                            background='black')  # id para cada item de archivo
            # actualizar totales: files ,dirs, kbytes
            gui_ppal.label_num_files.config(text=tl_files)
            gui_ppal.label_num_dirs.config(text=tl_dirs)
            gui_ppal.label_nombre_kb.config(text=f"{tl_size:,}")


# FUNCION: leer campo donde esta la ruta actual en el campo del combobox ventana principal
def leer_ruta(gui_ppal):
    try:
        ruta = gui_ppal.combobox_widget.get()
        os.chdir(ruta)  # nueva ruta
        curdir = os.getcwd()  # ruta actual
        print("Ruta actual:", curdir)
        gui_ppal.label_notice.configure(text="")  # info de estatus
        return os.listdir(curdir)
    except Exception as e:
        print(e)
        print('Error No existe ruta.')
        return None


# -*******************************************************************************
#   CLASE
# _*******************************************************************************
# CLASE principal para correr Controlador
class ControladorPPAL:

    def __init__(self):
        # atributos
        self.data = None
        self.ruta = None
        self.name = None
        self.es_dir = None
        self.temp = None
        self.nueva_ruta = None
        self.submenu_selec = None
        self.salida = None
        self.posicion = None

        # ruta donde esta programa IMPORTANTE, leera los otros componentes y clases para ubicarse en el sistema
        self.ruta_app = os.getcwd()  # ruta actual donde esta el programa
        self.lista_atajos = Rutas.leer_rutas_files(self.ruta_app)
        os.chdir(self.ruta_app)  # posicionarse en ruta de programa

        # CARGAR ventana principal
        self.root = Tk()
        self.gui_ppal = Ppal.Ventana(self.root, self.ruta_app)  # se pasa la ruta app para iconos relacionados

        # ---------------------------------------------------------------
        # CARGA INICIAL de tabla con archivos y directorios:
        self.lista_directorio = self.cargar_ruta_inicial()  # leer entrada de ruta
        cargar_tabla(self.lista_directorio, self.gui_ppal)  # carga de contenido de tabla widget

        # -----------------------------------------------------------------
        #    EVENTOS
        # -----------------------------------------------------------------
        self.gui_ppal.tree.bind("<<TreeviewSelect>>", self.click_seleccion)  # seleccionar fila en tabla
        self.gui_ppal.tree.bind("<Double-Button-1>", self.doble_click_tree)  # doble click a la tabla
        self.gui_ppal.btn_irRuta.bind("<Button-1>", self.btn_click_ruta)  # ir a ruta del campo combobox
        self.gui_ppal.combobox_widget.bind("<Return>", self.btn_click_ruta)  # Enter al campo de combobox ruta
        self.gui_ppal.btn_del.bind("<Button-1>", self.btn_borrar_un_archivo)  # borrar un solo archivo
        self.gui_ppal.btn_unFile.bind("<Button-1>", self.btn_renombrar_un_archivo)  # renombrar un solo archivo
        self.gui_ppal.btn_allFile.bind("<Button-1>", self.btn_renombrar_grupo_archivo)  # renombra grupos de archivos

        # ----------------------------------------------------------------
        # Asignacion de comandos para Submenu, los numeros son los index de items del menu
        self.gui_ppal.submenu1.entryconfig(0, command=self.accion_add_atajo)  # 0
        self.gui_ppal.submenu1.entryconfig(1, command=self.accion_quitar_atajo)  # 1
        self.gui_ppal.submenu1.entryconfig(3, command=lambda: self.btn_renombrar_un_archivo(None))  # 3
        self.gui_ppal.submenu1.entryconfig(4, command=lambda: self.btn_renombrar_grupo_archivo(None))  # 4
        self.gui_ppal.submenu1.entryconfig(5, command=lambda: self.btn_borrar_un_archivo(None))  # 5
        self.gui_ppal.submenu1.entryconfig(7, command=self.btn_acerca)  # 7
        self.gui_ppal.submenu1.entryconfig(8, command=lambda: self.root.quit())  # 8

    # ------------------------------------------------------------------------------------------------------------------
    # FUNCION: leer campo donde esta la ruta
    def cargar_ruta_inicial(self):
        if len(self.lista_atajos) is 0:  # si no hay items es 0
            self.gui_ppal.combobox_widget.set(self.ruta_app)  # pone la ruta del programa
        else:
            self.gui_ppal.combobox_widget['values'] = self.lista_atajos
            self.gui_ppal.combobox_widget.set(self.lista_atajos[0])
            try:
                os.chdir(self.lista_atajos[0])  # se posicionarse en la nueva ruta
            except Exception as e:
                print(e)
                print('Error No existe ruta [SE LEERA DIRECTORIO RAIZ DEL PROGRAMA..].')
                self.gui_ppal.combobox_widget.set(self.ruta_app)  # pone la ruta del programa

        curdir = os.getcwd()  # ruta actual
        return os.listdir(curdir)

    #  Evento selecccion (UN CLICK SOBRE TABLA) _event = se pone piso al declarar y no usar
    def click_seleccion(self, _event):
        print("[seleccion]")
        self.data = self.gui_ppal.tree.item(self.gui_ppal.tree.selection())
        print('data lista:', self.data)

        # colocar el nombre del archivo  campo borrar
        if hasattr(Borrar.DeleteOneFile.one_window_del, 'existe'):
            Borrar.DeleteOneFile.one_window_del.nombre_archivo.set(self.data['text'])  # actualizar campor Del

        #  colocar el nombre del archivo a campo renombrar
        if hasattr(RenUno.RenameOneFile.one_window_file, 'existe'):
            RenUno.RenameOneFile.one_window_file.nombre_archivo.set(self.data['text'])  # actualizar campo Rename

    # EVENTO APARECER VENTANA DE CAMPO para borrar un archivo
    def btn_borrar_un_archivo(self, _event):
        Borrar.DeleteOneFile.cargar(self.root, self.gui_ppal)

    # boton renombrar un solo Archivo
    def btn_renombrar_un_archivo(self, _event):
        RenUno.RenameOneFile.cargar(self.root, self.gui_ppal)

    # boton renombrar grupo de Archivo
    def btn_renombrar_grupo_archivo(self, _event):
        RenGrupo.RenameGrupoFile.cargar(self.root, self.gui_ppal)

    # Evento boton click para leer ruta de campo entrada
    def btn_click_ruta(self, _event):
        print("[Leer ruta]")
        try:
            self.lista_directorio = leer_ruta(self.gui_ppal)  # leer entrada de ruta
            cargar_tabla(self.lista_directorio, self.gui_ppal)  # carga de contenido de tabla
        except Exception as e:
            print(e)
            name = self.gui_ppal.combobox_widget.get()
            mb.showerror('Error', f'No se puede acceder al directorio:\n {name}')  # reporta error de dir
            print('Error de lectura..')

    # boton de submenu para acerca.
    def btn_acerca(self):
        Acerca.accion_acerca(self.root, self.ruta_app)

    #  Evento doble-click treeview (subir o bajar nivel directorio)
    def doble_click_tree(self, _event):
        self.data = self.gui_ppal.tree.item(self.gui_ppal.tree.selection())
        self.name = self.data['text']
        print("[doble click] => ", self.name)
        self.es_dir = os.path.isdir(self.name)  # confirmar si es un directorio
        if self.name == '..':
            self.ruta = self.gui_ppal.combobox_widget.get()
            self.temp = os.path.split(self.ruta)
            self.gui_ppal.combobox_widget.set(self.temp[0])  # ponemos la nueva ruta en el path
            self.lista_directorio = leer_ruta(self.gui_ppal)  # leer entrada de ruta
            cargar_tabla(self.lista_directorio, self.gui_ppal)  # carga de contenido de tabla
        elif self.es_dir:
            self.ruta = self.gui_ppal.combobox_widget.get()
            try:
                self.nueva_ruta = os.path.join(self.ruta, self.name)
                self.gui_ppal.combobox_widget.set(self.nueva_ruta)  # ponemos la nueva ruta en el path
                self.lista_directorio = leer_ruta(self.gui_ppal)  # leer entrada de ruta
                cargar_tabla(self.lista_directorio, self.gui_ppal)  # carga de contenido de tabla
            except Exception as e:
                print(e)
                self.gui_ppal.combobox_widget.set(self.ruta)
                self.lista_directorio = leer_ruta(self.gui_ppal)  # leer entrada de ruta
                cargar_tabla(self.lista_directorio, self.gui_ppal)  # carga de contenido de tabla
                mb.showerror('Error', f'No se puede acceder al directorio -> {self.name}')  # reporta error de dir
        else:  # En caso de no ser un directorio
            # previsualizacion
            mb.showinfo('Info File', ''
                                     'Previsualizacion \n NO DISPONIBLE...')  # pone separador de miles

    # FUNCION agregar ataja de ruta
    def accion_add_atajo(self):
        print("[agregar ATAJO]")
        self.ruta = self.gui_ppal.combobox_widget.get()
        self.lista_atajos.append(self.ruta)
        self.gui_ppal.combobox_widget['values'] = self.lista_atajos
        self.posicion = len(self.lista_atajos)
        self.gui_ppal.combobox_widget.current(self.posicion - 1)
        Rutas.guardar_rutas_files(self.ruta_app, self.lista_atajos)  # guardamos atajos de registro
        print("Salvando historico de rutas...")

    # FUNCION quitar atajos de ruta
    def accion_quitar_atajo(self):
        if len(self.lista_atajos) > 0:
            self.posicion = self.gui_ppal.combobox_widget.current()
            self.lista_atajos.pop(self.posicion)
            self.gui_ppal.combobox_widget['values'] = self.lista_atajos
            self.gui_ppal.combobox_widget.set('')  # limpiar campo combobox
            print("quitar ATAJO-", len(self.lista_atajos))
            Rutas.guardar_rutas_files(self.ruta_app, self.lista_atajos)  # guardamos atajos de registro
            print("Salvando historico de rutas...")
