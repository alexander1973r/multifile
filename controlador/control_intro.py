from tkinter import *
from vistas import vista_intro as introPRG  # importando la vista INTRO PROGRAMA


# CLASE controlador
class IntroProgram:
    window_INTRO = None

    # func para cargar la ventana
    @classmethod
    def cargar(cls, root, ruta_app, time=5):
        print('[Intro]')

        # ponemos Toplevel() para indicar que existe una ventana padre y se debe enfocar como hija
        cls.window_INTRO = Toplevel(root)  # asignar que es ventana hija
        cls.win_INTRO = introPRG.Ventana(cls.window_INTRO, ruta_app)  # instanciar Window_INTRO
        cls.window_INTRO.transient(root)
        cls.window_INTRO .grab_set()

        # tiempo de espera
        cls.inicio = time  # 5 seg y cierra la ventana

        def time():
            cls.inicio -= 1
            cls.win_INTRO.etiqueta_contador.config(text=cls.inicio)
            if cls.inicio == 0:
                cls.win_INTRO.cerrar_vent()
                print('[END intro]')
            cls.window_INTRO.after(1000, time)

        time()


#  testing 310702020
# CARGAR ventana principal
# import  os
# raiz = Tk()
# ruta = os.getcwd()
# ruta = os.path.join(ruta,'..')
# IntroProgram.cargar(raiz, ruta)
# raiz.mainloop()
