# Controlador renombrar un archivo
from tkinter import *
import os

# ---------------------------------------------
#  VISTA
from vistas import vista_deleteONEV1 as deleteONE  # importando la vista renombrar un solo archivo
# ----------------------------------------------
# CONTROLADOR
from controlador import control_principal as ppal  # funcion leer rutas
# -----------------------------------------------

# CLASE controlador para Renombrar un solo archivo
class DeleteOneFile:
    one_window_del = None
    gui_ppal = None

    # se usa cls a las variables que van a tener permanencia en los datos
    # func para cargar la ventana
    @classmethod
    def cargar(cls, root, gui_ppal):

        print('[renombrar ONE]')
        cls.data = gui_ppal.tree.item(gui_ppal.tree.selection())  # toma seleccion de fila de tabla

        if hasattr(cls.one_window_del, 'existe'):
            cls.window_two.focus()
            cls.one_window_del.nombre_archivo.set(cls.data['text'])
        else:
            # Se debe crear la raiz de la nueva ventana  afuera para que no vuelva a crear instancias
            # ponemos Toplevel()p para indicar que existe una ventana padre y se debe enfocar como hija
            cls.window_two = Toplevel(root)  # asignar que es ventana hija
            cls.one_window_del = deleteONE.Ventana(cls.window_two)  # instanciar Window_file DELETE
            cls.one_window_del.nombre_archivo.set(
                cls.data['text'])  # se pasa la ruta app para cargar los iconos relacionados

            cls.controles_para_one_delete(gui_ppal)  # cargar los eventos para la ventana delete

    @classmethod
    def controles_para_one_delete(cls, gui_ppal):
        # funcion cerrar ventana OneFile
        def accion_borrar_no():
            cls.one_window_del.cerrar_vent()

        # funcion borrar nombre de un archivo
        def accion_borrar_si(_event, gui):
            print('[cambiar Nombre]')
            ruta = gui.combobox_widget.get()
            old_file = os.path.join(ruta, cls.one_window_del.nombre_archivo.get())
            os.remove(old_file)

            # actualizar la lista
            directorio = ppal.leer_ruta(gui_ppal)
            ppal.cargar_tabla(directorio, gui_ppal)

        # eventos de Ventana renameONE
        cls.one_window_del.btn_si.bind("<Button-1>", lambda event, gui=gui_ppal: accion_borrar_si(event, gui))
        cls.one_window_del.btn_no.config(command=accion_borrar_no)  # para cerrar window usar command
