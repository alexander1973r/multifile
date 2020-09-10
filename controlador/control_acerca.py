# Controlador de Acerca
from tkinter import *

# -----------------------------------
# VISTAS
from vistas import vista_acercaV1 as acercaWIN

window_acerca = None
win_acerca = None


# funcion para mostrar ventana acerca.
def accion_acerca(root, ruta_app):
    global win_acerca
    global window_acerca

    if hasattr(win_acerca , 'existe'):
        window_acerca.focus()
    else:
        window_acerca = Toplevel(root)  # asignar que es ventana hija
        win_acerca = acercaWIN.Ventana(window_acerca, ruta_app)  # instancia Window

        # controles_para_acerca()

        # acciones
        def accion_acerca_ver(_event):
            win_acerca.tabControl.select(0)

        def accion_sugerencia(_event):
            win_acerca.tabControl.select(1)

        def accion_licencia(_event):
            win_acerca.tabControl.select(2)

        def accion_salir(_event):
            win_acerca.cerrar_vent()

        # eventos de Ventana renameONE
        win_acerca.btn_acerca.bind("<Button-1>", accion_acerca_ver)
        win_acerca.btn_sugerencia.bind("<Button-1>", accion_sugerencia)
        win_acerca.btn_licencia.bind("<Button-1>", accion_licencia)
        win_acerca.btn_salir.bind("<Button-1>", accion_salir)
        # cls.one_window_del.btn_no.config(command=accion_borrar_no)  # para cerrar window usar command



# Probador de ventana
# import os
# raiz = Tk()
# ruta = os.getcwd()
# ruta = os.path.join(ruta,'..')
# accion_acerca(raiz, ruta)
# raiz.mainloop()