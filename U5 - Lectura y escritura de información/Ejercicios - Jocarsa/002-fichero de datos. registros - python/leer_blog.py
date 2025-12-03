'''
Programa: Lector de Blog v0.1

Gustavo Delnardo

Vamos a leer artículos de un blog desde un archivo JSON y mostrarlos en consola y en HTML. En este ejercicio aprenderemos a leer información de un archivo JSON y mostrarla de manera organizada. Simularemos un blog de videojuegos, donde cada artículo es un registro en JSON. Esto nos permite practicar manejo de ficheros y estructuras de datos, fundamentales para el desarrollo web.
'''

import json  # Librería estándar para trabajar con JSON

# Abrir y leer el archivo JSON
try:
    with open("blog.json", "r", encoding="utf-8") as archivo:
        articulos = json.load(archivo)  # Cargar el contenido del JSON
except FileNotFoundError:
    print("El archivo blog.json no existe.")
    articulos = []

# Mostrar los artículos en consola
print("\n--- Artículos del blog ---")
for articulo in articulos:
    print("Título:", articulo["titulo"])
    print("Fecha:", articulo["fecha"])
    print("Autor:", articulo["autor"])
    print("Contenido:", articulo["contenido"])
    print("---------------------------")


#Con este ejercicio aprendimos a leer datos desde un archivo JSON y procesarlos con Python. Vimos cómo convertir estos datos en una página web simple en HTML para mostrarlos de manera clara. Este concepto es útil para desarrollar blogs, catálogos o cualquier aplicación web que necesite mostrar información dinámica.
