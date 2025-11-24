"""
Programa: Gestión de Archivos y ZIP v0.1
Autor: Gustavo Delnardo
Aprender a crear, comprimir y eliminar archivos es fundamental para mantener tus datos organizados.
En este ejercicio gestionaremos una lista de juegos en un archivo de texto, que luego comprimiremos y eliminaremos. Estas habilidades son útiles para organizar tus videojuegos, música o cualquier tipo de archivos digitales.
"""

import os
import zipfile

# ------------------------------
# CREAR EL ARCHIVO DE TEXTO
# ------------------------------
nombre_archivo = "lista_de_juegos.txt"

#abrimos el archivo en modo escritura
with open(nombre_archivo, "w", encoding="utf-8") as archivo:
    archivo.write("1. The Legend of Zelda\n")
    archivo.write("2. Super Mario Odyssey\n")
    archivo.write("3. Minecraft\n")
print(f"Archivo '{nombre_archivo}' creado con éxito.")

# ------------------------------
# COMPRIMIR EL ARCHIVO EN ZIP
# ------------------------------
nombre_zip = "games.zip"

with zipfile.ZipFile(nombre_zip, "w") as archivo_zip:
    archivo_zip.write(nombre_archivo)
print(f"Archivo '{nombre_archivo}' comprimido en '{nombre_zip}'.")

# ------------------------------
# ELIMINAR EL ARCHIVO DE TEXTO
# ------------------------------
def eliminar_archivo(ruta):
    if os.path.exists(ruta):
        os.remove(ruta)
        print(f"Archivo '{ruta}' eliminado.")
    else:
        print(f"El archivo '{ruta}' no existe, no se puede eliminar.")

eliminar_archivo(nombre_archivo)

#open(..., "w") → Crea el archivo de texto y permite escribir en él.

#zipfile.ZipFile(..., "w") → Crea un archivo ZIP y añade archivos dentro.

#os.remove() → Elimina el archivo de texto después de comprimirlo.

#os.path.exists() → Verifica que el archivo existe antes de eliminarlo para evitar errores.

#Con este ejercicio aprendimos a crear, comprimir y eliminar archivos de manera segura en Python. Vimos cómo organizar datos de juegos y música y cómo reducir espacio usando ZIP. Estas habilidades son esenciales para gestionar y mantener organizados los archivos en proyectos reales.
