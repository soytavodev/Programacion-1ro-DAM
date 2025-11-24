"""
Gestión de Archivos v0.1
Gustavo Delnardo

Aprender a escribir y leer archivos es fundamental para almacenar información de manera persistente en programas. En este ejercicio, vamos a guardar mensajes y usuarios de un juego de música en archivos de texto y binarios. Esto nos permitirá practicar cómo gestionar datos de manera organizada y segura en Python.
"""

# ------------------------------
# PARTE 1: ARCHIVO DE TEXTO
# ------------------------------

#abrimos el archivo bienvenida.txt en modo "w" para escribir
archivo_texto = open("bienvenida.txt", "w", encoding="utf-8")
archivo_texto.write("¡Bienvenido al Juego de Música!\n")  #primera línea
archivo_texto.write("Juega y disfruta\n")  #segunda línea
archivo_texto.close()  #cerramos el archivo

#leemos el contenido del archivo
archivo_texto = open("bienvenida.txt", "r", encoding="utf-8")
lineas = archivo_texto.readlines()
archivo_texto.close()

#mostramos el contenido
print("--- Contenido de bienvenida.txt ---")
for linea in lineas:
    print(linea.strip())

# ------------------------------
# PARTE 2: ARCHIVO BINARIO
# ------------------------------

#clase Usuario
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

#crear dos usuarios
usuario1 = Usuario("Gustavo", "gustavo1@gmail.com")
usuario2 = Usuario("Ana", "ana1@gmail.com")

#guardar usuarios en archivo binario
archivo_binario = open("usuarios.bin", "wb")
archivo_binario.write(f"{usuario1.nombre},{usuario1.email}\n".encode("utf-8"))
archivo_binario.write(f"{usuario2.nombre},{usuario2.email}\n".encode("utf-8"))
archivo_binario.close()

#leer archivo binario
archivo_binario = open("usuarios.bin", "rb")
contenido_binario = archivo_binario.readlines()
archivo_binario.close()

#mostrar usuarios
print("\n--- Usuarios del archivo binario ---")
for linea in contenido_binario:
    datos = linea.decode("utf-8").strip().split(",")
    print(f"Nombre: {datos[0]}, Email: {datos[1]}")

