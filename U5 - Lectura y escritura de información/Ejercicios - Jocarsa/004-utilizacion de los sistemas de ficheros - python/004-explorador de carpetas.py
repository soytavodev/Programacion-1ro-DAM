'''
Explorador de Carpetas v0.1

Gustavo Delnardo

Descripción: Recorre una carpeta y muestra el contenido con tamaños de archivos en MB, filtrando los mayores a 1 GB.

Trabajar con sistemas de ficheros permite organizar, leer y analizar los archivos y carpetas de tu ordenador.
En este ejercicio vamos a recorrer una carpeta indicada por el usuario y mostrar información de cada archivo, incluyendo tamaño y nombre. Esto es útil para gestionar juegos, música u otros archivos grandes de manera eficiente.
'''

import os  #librería estándar para manejar sistemas de ficheros

#pedimos al usuario que indique la ruta de la carpeta a explorar
carpeta = input("Introduce la ruta de la carpeta que quieres explorar: ")

#recorremos la carpeta incluyendo subcarpetas
for ruta_actual, subdirs, archivos in os.walk(carpeta):
    print(f"\nExplorando la carpeta: {ruta_actual}")
    
    for archivo in archivos:
        ruta_archivo = os.path.join(ruta_actual, archivo)  #obtenemos la ruta completa
        tamaño_bytes = os.path.getsize(ruta_archivo)       #tamaño en bytes
        tamaño_MB = tamaño_bytes / (1024 * 1024)          #convertimos a MB
        
        print(f"Archivo: {archivo} - Tamaño: {tamaño_MB:.2f} MB")
        
        #filtramos archivos mayores a 1 GB
        if tamaño_bytes > (1024 * 1024 * 1024):
            tamaño_GB = tamaño_bytes / (1024 * 1024 * 1024)
            print(f"*** Archivo grande (>1GB): {archivo} - {tamaño_GB:.2f} GB ***")
						
						#os.walk(carpeta) → Recorre la carpeta y todas sus subcarpetas.

						#os.path.join() → Crea la ruta completa de cada archivo.

						#os.path.getsize() → Obtiene el tamaño del archivo en bytes.

						#Convertimos bytes a MB o GB para mostrar los tamaños de manera legible.

						#El programa filtra archivos mayores a 1 GB, destacándolos en la salida.


#Con este ejercicio aprendimos a navegar y explorar sistemas de ficheros usando Python. Vimos cómo calcular tamaños y filtrar archivos grandes, útil para gestionar juegos o colecciones de música. Estas habilidades son esenciales para automatizar la gestión de archivos y analizar datos en proyectos reales.

