import os  # modulo para manejar archivos del so


# Esta funcion se encarga de leer el historico y atajos de las rutas
# leer
def leer_rutas_files(ruta):
    try:
        # Leer linea por linea
        file_to_read = os.path.join(ruta, 'modelos', 'rutas.txt')
        print('leyendo...', file_to_read)
        archivo = open(file_to_read, mode='r', encoding='utf-8')  # Leer archivo con chars UTF8
        # inicia bucle infinito para leer línea a línea
        lista = []
        while True:
            linea = archivo.readline()  # lee línea
            if not linea:
                break  # Si no hay más se rompe bucle
            lista.append(linea.replace('\n', ''))

        archivo.close()  # Cierra archivo
        print(lista)
        return lista
    except Exception as e:
        print(e)
        print('Error no existe archivo de Rutas para leer')
        return []


# guardar
def guardar_rutas_files(ruta, lista):
    print('guardando...')
    ruta_guardar = os.path.join(ruta, 'modelos', 'rutas.txt')
    archivo = open(ruta_guardar, mode='w', encoding='utf-8')  # creando archivo para escritura UNICODE
    for item in lista:
        # registrar datos
        archivo.write(item + "\n")  # data + new line

    archivo.close()  # Cierra archivo
