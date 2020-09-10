# Controlador renombrar un archivo

# -----------------------------------
# # VISTAS
from vistas import vista_renameONEV1 as renameONE  # importando la vista renombrar un solo archivo

# -----------------------------------
# CONTROLADOR
from controlador.control_principal import *  # funcion leer rutas


# CLASE controlador para Renombrar un solo archivo
class RenameOneFile:
    one_window_file = None

    # func para cargar la ventana
    @classmethod
    def cargar(cls, root, gui_ppal):
        print('[Renombrar ONE]')
        # codigo que detecta si existe la ventana (solo crea una)
        cls.data = gui_ppal.tree.item(gui_ppal.tree.selection())  # toma seleccion de fila de tabla

        if hasattr(cls.one_window_file, 'existe'):
            cls.window_one.focus()
            cls.one_window_file.nombre_archivo.set(cls.data['text'])
            cls.one_window_file.nombre_archivo_viejo = cls.data['text']
        else:
            cls.window_one = Toplevel(root)  # asignar que es ventana hija
            cls.one_window_file = renameONE.Ventana(cls.window_one)  # instanciar Window_file
            cls.one_window_file.nombre_archivo.set(cls.data['text'])  # se pasa la ruta app
            # para cargar los iconos  relacionados
            cls.one_window_file.nombre_archivo_viejo = cls.data['text']
            cls.controles_para_one_rename(gui_ppal)  # eventos de la ventana renombrar un archivo

        # try:
        #     # pregunta si existe lo pone en foco
        #     if cls.window_one.state() == "normal":
        #         cls.window_one.focus()
        #         cls.one_window_file.nombre_archivo.set(cls.data['text'])
        #         cls.one_window_file.nombre_archivo_viejo = cls.data['text']
        # except Exception as e:
        #     print(e)
        #     # Se debe crear la raiz de la nueva ventana  afuera para que no vuelva a crear instancias
        #     # ponemos Toplevel() para indicar que existe una ventana padre y se debe enfocar como hija
        #     cls.window_one = Toplevel(root)  # asignar que es ventana hija
        #     cls.one_window_file = renameONE.Ventana(cls.window_one)  # instanciar Window_file
        #     cls.one_window_file.nombre_archivo.set(cls.data['text'])  # se pasa la ruta app
        #     # para cargar los iconos  relacionados
        #     cls.one_window_file.nombre_archivo_viejo = cls.data['text']
        #
        #     cls.controles_para_one_rename(gui_ppal)  # eventos de la ventana renombrar un archivo

    @classmethod
    def controles_para_one_rename(cls, gui_ppal):

        # funcion cerrar ventana OneFile
        def accion_no():
            cls.one_window_file.cerrar_vent()

        # funcion cambiar nombre a un archivo
        def accion_si(_event, gui):
            print('[cambiar Nombre]')
            ruta = gui.combobox_widget.get()
            old_file = os.path.join(ruta, cls.one_window_file.nombre_archivo_viejo)
            new_file = os.path.join(ruta, cls.one_window_file.nombre_archivo.get())
            data = gui.tree.item(gui.tree.selection())  # toma seleccion de fila de tabla
            #  print(old_file,'<-->', new_file) # testing
            os.rename(old_file, new_file)
            # actualizar la lista y remarcar nombre cambiado en lista
            i = data["tags"][0]  # toma el valor tag para resaltar archivo cambiado
            gui.tree.item(gui.tree.selection(), text=cls.one_window_file.nombre_archivo.get())
            print(i)
            gui.tree.tag_configure(i, background='Yellow', foreground='black')

        # eventos de Ventana renameONE ( se usa lambda para pasar parametros a funcion llamada por bind
        cls.one_window_file.btn_si.bind("<Button-1>", lambda event, gui=gui_ppal: accion_si(event, gui))
        cls.one_window_file.btn_no.config(command=accion_no)  # para cerrar window usar command
