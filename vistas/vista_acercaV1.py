from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # se usa para ajustar imagen
import os

# ACERCA  ---> contenido
# --------------------------------------------------------------------------
acerca = """                    
MultiFile Ver. 1.0

Gracias por la oportunidad y tiempo de usar mi programa.
 
Con tu aporte, me ayudas a seguir creciendo como profesional, 
financiar este proyecto, darle rentabilidad y objetivo para mejorarlo 
cada dia para que sea una herramienta util para todos.

Tus opinionens y sugerencias son importantes y se tomaran en cuenta 
para ir creciendo este proyecto con el aporte de ideas de cada uno de 
los usuarios que apoyen este proyecto.

Cualquier donacion pueden hacerlo por:


Patreon:

www.patreon.com/alexander4096

Paypal: 

alexander4096@yahoo.es

Sugerencias:

Email: alexander1973r@gmail.com


OBJETIVO DE ESTE PROYECTO: 

Version 1.0

El programa se hizo inicialmente para facilitar la accion de renombrar los
archivos en bloques del mismo nivel de ruta, al permitir buscar 
coincidencias y  reemplazarlo con la palabra propuesta por el usuario.

Se permite tambien cambiar el nombre de un solo archivo y 
borrar archivos, En las versiones  siguientes se van agregar 
mas funcionalidades, las cuales pueden aparecer en las 
sugerencias de acuedo al plantemiento e ideas aportados 
por la comunidad.

Se dispone del codigo fuente hecho en Python / Tkinter para todo aquel 
interesado en estudiarlo y conocer la sintaxis implementada en los 
widgets de tkinter, clases y metodos usados, bien sea para mejorar 
el programa o tomar ideas para su propio proyecto

"""
# --------------------------------------------------------------------------


# Cosas por hacer ---> contenido
# --------------------------------------------------------------------------
sugerencias = """
Sugererencias por Hacer

1. Boton para copiar y pegar archivos en otros directorios
2. Boton para corta y pegar archivos en otros directorios
3. Historico de cambios en los nombres de archivo para poder reversar la
   accion al anterior nombre.
4. Personalizar cuales botones seran colocados como acceso directo en la
   parte superior del menu.
5. Permitir previsualizar archivo de texto plano al seleccionarlo.
6. Permitir previsualozar archivo de fotos al seleccionarlo
7. Accion para ajustar tamaño de imagenes en bloques de archivos 
   seleccionados.
8. Ordenar la lista de la tabla en forma ascendente y descendente
9. Filtrar la visualizacion de contenido de un directorio
10. Buscar un archivo
11. Personalizar el tipo de unidad de almacenamiento usado, kb, mb, gb
12. Ver los archivos y directorios en bloques de iconos
13. Agregar boton de ayuda
14. Hacer multilenguaje la interface
15. El borrado de archivo notifique a la papelara de reciclaje de windows

Cualquier sugerencia para mejorar el programa puede enviarlo al email:

  alexander1973r@gmail.com
"""
# --------------------------------------------------------------------------


# Licencia ---> contenido
# --------------------------------------------------------------------------
licencia = """La MIT Licencia.
         
              Copyright (c) <2020> <copyright holders>

Por la presente se otorga permiso, sin cargo, a cualquier persona que obtenga 
una copia de este software y los archivos de documentación asociados 
(el "Software"),  para tratar en el Software sin restricción, incluidos, 
entre otros, los derechos para usar, copiar, modificar, fusionar, publicar, 
distribuir, sublicenciar y / o  vender copias del Software y para permitir 
a las personas a quienes pertenece el Software amueblado para hacerlo, 
sujeto a las siguientes condiciones:

El aviso de copyright anterior y este aviso de permiso se incluirán en todos
copias o porciones sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O
IMPLÍCITO, INCLUYENDO PERO NO LIMITADO A LAS GARANTÍAS DE COMERCIABILIDAD,
APTITUD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO EL
LOS AUTORES O LOS TITULARES DE LOS DERECHOS DE AUTOR SERÁN RESPONSABLES POR 
CUALQUIER RECLAMACIÓN, DAÑO U OTRO RESPONSABILIDAD, EN CASO DE ACCIÓN DE 
CONTRATO, TORTURA O DE OTRA MANERA, DERIVADA DE, FUERA DE O EN CONEXIÓN 
CON EL SOFTWARE O EL USO U OTRAS OFERTAS EN EL SOFTWARE.

Programador:

   Alexander Rodriguez.
   Email: alexander1973r@gmail.com
   Twitter: @alexander4096
   Linkedin: https://www.linkedin.com/in/alexander4096/
   
"""


# clase para ventana de Acerca
class Ventana:
    def __init__(self, root, ruta_app):
        self.existe = False

        # crear ventana de aviso
        self.existe = True
        self.root = root  # asignar ventana
        self.root.title('Acerca del programa Multifile')
        self.root.config(bg="black")
        self.root.geometry("650x450")  # tamaño y posicion
        self.root.minsize(width=650, height=450)
        # self.root.resizable(width=FALSE) # no redimensiona
        self.root.attributes("-topmost", True)  # colocar al frente la ventana

        # construccion de las pestañas de tabulacion
        self.tabControl = ttk.Notebook(self.root)
        self.tab1 = Frame(self.tabControl)  # 0
        self.tab2 = Frame(self.tabControl)  # 1
        self.tab3 = Frame(self.tabControl)  # 2

        self.tabControl.add(self.tab1, text=' Acerca... ')
        self.tabControl.add(self.tab2, text=' Sugerencias ')
        self.tabControl.add(self.tab3, text=' Licencia ')
        self.tabControl.pack(expand=1, fill="both")

        # texto de acerca -------------------------------------------------------
        self.texto_tab1 = Text(self.tab1, height=10, width=80)
        self.texto_tab1.insert(1.0, acerca)
        self.texto_tab1.config(state=DISABLED)

        #  IMAGEN De cabecera  "imagen/LOGOprogramMultifile.jpg"  <-- para vista
        #  ../vistas/imagen/LOGOprogramMultifile.jpg  <=== ruta cuando se llama desde el controlador
        self.ruta_foto = os.path.join(ruta_app, 'vistas', 'imagen',
                                      'LOGOprogramMultifile.jpg')  # ruta donde esta el app + icono

        self.img5 = Image.open(self.ruta_foto)  # se usa otra variable
        self.img5 = self.img5.resize((500, 300), Image.ANTIALIAS)
        self.img5 = ImageTk.PhotoImage(self.img5)  # convert to PhotoImage
        self.texto_tab1.image_create(1.0, image=self.img5)  # poner foto

        # formateo de texto
        self.texto_tab1.tag_add("texto", "1.0", END)
        self.texto_tab1.tag_config("texto", font=('Arial', 14),
                                   justify=CENTER, spacing2=5)

        # Scroll Y
        self.textYScroll = Scrollbar(self.tab1, orient=VERTICAL)
        self.textYScroll.configure(command=self.texto_tab1.yview)
        self.texto_tab1.configure(yscrollcommand=self.textYScroll.set)
        self.textYScroll.pack(side=RIGHT, fill=Y)  # pack scroll
        self.texto_tab1.pack(fill=BOTH, expand=1)  # pack texto

        # texto Sugerencias  ----------------------------------------------
        self.texto_tab2 = Text(self.tab2, height=10, width=80)
        self.texto_tab2.insert(1.0, sugerencias)
        self.texto_tab2.config(state=DISABLED)

        #  IMAGEN De cabecera imagen/LogoPersonalProgramadorV2.png" <-- ruta cuando se llama desde vistas
        # ../vistas/imagen/LogoPersonalProgramadorV2.png <== ruta cuando se llama desde el controlador
        self.ruta_foto = os.path.join(ruta_app, 'vistas', 'imagen',
                                      'LogoPersonalProgramadorV2.png')  # ruta donde esta el app + icono

        self.img6 = Image.open(self.ruta_foto)  # se usa otra variable
        self.img6 = self.img6.resize((600, 150), Image.ANTIALIAS)
        self.img6 = ImageTk.PhotoImage(self.img6)  # convert to PhotoImage
        #  self.photo = PhotoImage(file=r'iconos/borrar.png')
        self.texto_tab2.image_create(1.0, image=self.img6)  # poner foto
        # self.tabControl.select(1)

        # formateo de texto
        self.texto_tab2.tag_add("titulo", "1.0", "2.26")
        self.texto_tab2.tag_config("titulo", font=('Arial', 14, 'bold'),
                                   justify=CENTER, spacing2=5)

        # Scroll Y
        self.textYScroll = Scrollbar(self.tab2, orient=VERTICAL)
        self.textYScroll.configure(command=self.texto_tab2.yview)
        self.texto_tab2.configure(yscrollcommand=self.textYScroll.set)
        self.textYScroll.pack(side=RIGHT, fill=Y)  # pack scroll
        self.texto_tab2.pack(fill=BOTH, expand=1)  # pack texto

        # texto de Licencia----------------------------------------
        self.texto_tab3 = Text(self.tab3, height=10, width=80)
        self.texto_tab3.insert(1.0, licencia)
        self.texto_tab3.config(state=DISABLED)
        # formateo de texto
        self.texto_tab3.tag_add("subtitulo", "1.0", "1.16")
        self.texto_tab3.tag_config("subtitulo", font=('Arial', 14, 'bold', 'italic'), spacing1=10)
        self.texto_tab3.tag_add("titulo", "3.0", "3.54")
        self.texto_tab3.tag_config("titulo", font=('Arial', 14, 'bold'))
        self.texto_tab3.tag_add("programador", "24.0", "24.12")
        self.texto_tab3.tag_config("programador", font=('Arial', 11, 'bold'), spacing2=5)
        # Scroll Y
        self.textYScroll = Scrollbar(self.tab3, orient=VERTICAL)
        self.textYScroll.configure(command=self.texto_tab3.yview)
        self.texto_tab3.configure(yscrollcommand=self.textYScroll.set)
        self.textYScroll.pack(side=RIGHT, fill=Y)  # pack scroll
        self.texto_tab3.pack(fill=BOTH, expand=1)  # pack texto

        # botones
        self.btn_acerca = Button(self.root, text="Acerca", width=8, font=("arial", 10))
        self.btn_acerca.pack(anchor=SE, side=LEFT, padx=10, pady=10)
        self.btn_sugerencia = Button(self.root, text="Sugerencia", width=8, font=("arial", 10))
        self.btn_sugerencia.pack(anchor=SE, side=LEFT, padx=10, pady=10)
        self.btn_licencia = Button(self.root, text="Licencia", width=8, font=("arial", 10))
        self.btn_licencia.pack(anchor=SE, side=LEFT, padx=10, pady=10)
        self.btn_salir = Button(self.root, text="Salir", width=8, font=("arial", 10))
        self.btn_salir.pack(anchor=SE, side=RIGHT, padx=10, pady=10)

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
# probador de ventana
# root = Tk()
# ruta = os.getcwd()  # ruta actual
# ruta  = os.path.join(ruta, '..')
# gui_ppal = Ventana(root, ruta)
# root.mainloop()
