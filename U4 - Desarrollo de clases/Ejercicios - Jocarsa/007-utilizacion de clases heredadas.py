'''
Tienda Digital v0.1

Autor: Gustavo Delnardo

Descripción: Gestión de productos digitales usando clases heredadas en Python.
En este ejercicio vamos a utilizar clases heredadas para representar productos digitales como videojuegos y música. Aprenderemos a crear una clase base y extenderla con clases hijas que añaden atributos específicos. Esto nos permite organizar el código y reutilizar atributos comunes de forma eficiente.
'''

# ----------- CLASE PADRE -----------
class Producto:
    #constructor para inicializar los atributos comunes de todos los productos
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# ----------- CLASES HIJAS -----------

#clase hija para videojuegos
class Videojuego(Producto):
    def __init__(self, nombre, precio, plataforma):
        super().__init__(nombre, precio)  #hereda nombre y precio de Producto
        self.plataforma = plataforma      #atributo exclusivo de Videojuego

#clase hija para música
class Musica(Producto):
    def __init__(self, nombre, precio, artista):
        super().__init__(nombre, precio)  #hereda nombre y precio de Producto
        self.artista = artista            #atributo exclusivo de Musica

# ----------- BLOQUE PRINCIPAL DEL PROGRAMA -----------

#crear instancias de las clases hijas
juego1 = Videojuego("Resident Evil", 60, "PC")
disco1 = Musica("Thriller", 20, "Michael Jackson")

#mostrar la información de los productos
print("--- Información del Videojuego ---")
print("Nombre:", juego1.nombre)
print("Precio:", juego1.precio, "euros")
print("Plataforma:", juego1.plataforma)

print("\n--- Información del Disco de Música ---")
print("Nombre:", disco1.nombre)
print("Precio:", disco1.precio, "euros")
print("Artista:", disco1.artista)


#Con este ejercicio aprendimos a usar herencia en Python para crear clases hijas que comparten atributos de una clase base. Vimos cómo agregar atributos específicos a cada tipo de producto, manteniendo el código organizado y reutilizable. Esto es útil para desarrollar tiendas en línea donde diferentes productos comparten características pero también tienen atributos únicos.


