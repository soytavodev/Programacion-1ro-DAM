'''
Clases

Gustavo Delnardo

En este ejercicio aprendemos a usar las clases en Python para representar entidades del mundo real, en este caso, clientes de una empresa.
Las clases nos permiten organizar la información y trabajar con objetos de manera más ordenada y reutilizable.
'''

#definición de la clase Cliente
class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

#creación de dos objetos de la clase Cliente
cliente1 = Cliente("Gustavo", "gustavo1@gmail.com")
cliente2 = Cliente("Pedro", "pedro1@gmail.com")

#impresión de la información de los clientes
print("Cliente 1:")
print("Nombre:", cliente1.nombre)
print("Email:", cliente1.email)

print("\nCliente 2:")
print("Nombre:", cliente2.nombre)
print("Email:", cliente2.email)

#con este ejercicio comprendemos cómo definir una clase y crear objetos a partir de ella, aprendemos también a asignar atributos y mostrar la información de forma clara. Estos fundamentos son esenciales para manejar datos en proyectos más complejos, como videojuegos o tiendas virtuales.
