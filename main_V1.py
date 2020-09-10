# carga de controladores PRINCIPALES PARA INICIAR
# usar python 3.6
from controlador.control_principal import ControladorPPAL
from controlador.control_intro import IntroProgram


if __name__ == "__main__":
    Iniciar = ControladorPPAL()
    print('Run...')            # corriendo
    IntroProgram.cargar(Iniciar.root, Iniciar.ruta_app, 5)   # ventana de intro 5seg
    Iniciar.root.mainloop()
    print('[bye]...')
