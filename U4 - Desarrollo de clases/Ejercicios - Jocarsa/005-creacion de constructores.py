'''
ContactManager v0.1

Gustavo Delnardo

Descripción: Gestión de información de clientes utilizando constructores con parámetros en Python.
En este ejercicio aprenderemos a usar constructores con parámetros para crear objetos de forma rápida y organizada. Simularemos una lista de contactos digitales, donde cada cliente tiene nombre, apellidos, email y dirección. Esto nos permitirá comprender cómo inicializar los atributos de un objeto directamente al momento de crearlo.
'''

#definición de la clase Cliente
class Cliente:
    #constructor con parámetros para inicializar los atributos del cliente
    def __init__(self, nombre, apellidos, email, direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion

# ----------- BLOQUE PRINCIPAL DEL PROGRAMA -----------

#pedimos los datos del cliente al usuario
nombre_cliente = input("Introduce el nombre del cliente: ")
apellidos_cliente = input("Introduce los apellidos del cliente: ")
email_cliente = input("Introduce el email del cliente: ")
direccion_cliente = input("Introduce la dirección del cliente: ")

#creamos un objeto Cliente usando el constructor con los datos introducidos
cliente1 = Cliente(nombre_cliente, apellidos_cliente, email_cliente, direccion_cliente)

#mostramos la información del cliente
print("\n--- Información del cliente ---")
print("Nombre:", cliente1.nombre)
print("Apellidos:", cliente1.apellidos)
print("Email:", cliente1.email)
print("Dirección:", cliente1.direccion)


#aprendimos a crear un cliente directamente con todos sus atributos y a mostrar su información en pantalla. Esto es útil para gestionar datos de usuarios o contactos de forma clara y organizada en cualquier proyecto de software.
