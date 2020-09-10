# Controlador renombrar un archivo
from tkinter import *  # libreria tkinter
from tkinter import messagebox as mb  # submodulo de messegebox
import os  # os para leer archivos y directorios

# -----------------------------------
# VISTAS
from vistas import vista_renameGROUPV1 as renGROUP  # importando la vista renombrar en grupos

# -----------------------------------
# CONTROLADOR
from controlador import control_principal as ControlPpal


# CLASE controlador para Renombrar un solo archivo
class RenameGrupoFile:
    archivo_encontrados = None
    win_renGROUP = None
    gui_ppal = None

    # func para cargar la ventana
    @classmethod
    def cargar(cls, root, gui_ppal):
        print('[Renombrar Grupo]')
        cls.archivo_encontrados = []  # arreglo para listado de archivos encontrados
        # codigo que detecta si existe la ventana (solo crea una)

        if hasattr(cls.win_renGROUP, 'existe'):
            cls.window_renGROUP.focus()
        else:
            # ponemos Toplevel() para indicar que existe una ventana padre y se debe enfocar como hija
            cls.window_renGROUP = Toplevel(root)  # asignar que es ventana hija
            cls.win_renGROUP = renGROUP.Ventana(cls.window_renGROUP)  # instanciar Window_renGROUP
            cls.controles_para_group_rename(gui_ppal)  # eventos de la ventana renombrar grupos

    #  accion salir
    @classmethod
    def accion_salir_grupo(cls, _event):
        cls.win_renGROUP.cerrar_vent()

    @classmethod
    def controles_para_group_rename(cls, gui_ppal):

        #  EVENTOS de la ventana renombrar en grupo
        cls.win_renGROUP.btn_si.bind("<Button-1>", lambda event, gui=gui_ppal: accion_buscar_grupo(event, gui))
        cls.win_renGROUP.btn_no_salir.bind("<Button-1>", cls.accion_salir_grupo)
        cls.win_renGROUP.btn_aplicar.bind("<Button-1>",
                                          lambda event, gui=gui_ppal: accion_aplicar_cambio(event, gui))

        #  accion para buscar  ARCHIVOS  items por condicion
        def accion_buscar_grupo(_event, gui):
            cls.archivo_encontrados = []
            lista_directorio = ControlPpal.leer_ruta(gui)  # leer entrada de ruta
            ControlPpal.cargar_tabla(lista_directorio, gui)  # carga de contenido de tabla
            print(lista_directorio)
            buscar_por = cls.win_renGROUP.archivo_buscar.get()
            # hay criterio para buscar archivos
            if len(buscar_por) == 0:
                mb.showwarning('Error', 'El campo a buscar debe tener un valor')
            else:
                # recorrido de directorio
                for i, archivo in enumerate(lista_directorio):
                    # buscar nombre de archivo
                    buscar = archivo.find(buscar_por)
                    if buscar > -1:
                        indice = gui.tree.get_children()[i]
                        # agregar al arreglo indice de archivo encontrado
                        cls.archivo_encontrados.append([archivo, i, indice])
                        gui.tree.tag_configure(i, foreground="black", background='Yellow')
                # termina el recorrido y reporta resultados
                if len(cls.archivo_encontrados) > 0:
                    cls.win_renGROUP.descripcion.configure(
                        text=f'Se han encontrado \n Items : {len(cls.archivo_encontrados)}', fg="white")
                else:
                    cls.win_renGROUP.descripcion.configure(
                        text=f'NO SE HA ENCONTRADO COINCIDENCIAS', fg="yellow")

        # ACCION para renombrar archivos en grupos
        def accion_aplicar_cambio(_event, gui):
            # leer nuevamente campos de datos
            cambiar_por = cls.win_renGROUP.archivo_cambiar.get()  # lee campo de cambio
            buscar_por = cls.win_renGROUP.archivo_buscar.get()
            # realizar cambios de nombre en grupos
            for archivo, i, indice in cls.archivo_encontrados:
                print(archivo, i)
                nuevo_nombre = archivo.replace(buscar_por, cambiar_por)
                # cambiando nombre en tabla
                print('[viejo Nombre]->', archivo, '[nuevo nombre]->', nuevo_nombre)
                gui.tree.item(indice, text=nuevo_nombre)
                gui.tree.tag_configure(i, background='Green', foreground='white')
                # renombrar el archivo fisicamente
                ruta = gui.combobox_widget.get()
                old_file = os.path.join(ruta, archivo)
                new_file = os.path.join(ruta, nuevo_nombre)
                os.rename(old_file, new_file)
