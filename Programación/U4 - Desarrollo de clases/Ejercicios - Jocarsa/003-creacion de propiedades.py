'''
Client Manager v0.1

Gustavo Delnardo

Descripción: Gestión de información de clientes (nombre, edad y teléfonos)
utilizando propiedades (getters y setters) en Python.

En este ejercicio aprenderemos a crear propiedades (properties) para controlar el acceso y la modificación de los atributos de una clase. Simularemos una tienda de videojuegos donde gestionaremos los datos de un cliente y sus teléfonos. El objetivo es entender cómo las propiedades permiten mantener la encapsulación y seguridad de los datos sin complicar el uso de la clase.
'''

# Definición de la clase Cliente
class Cliente:
    # Método constructor
    def __init__(self):
        self.__nombre = ""      # atributo privado para el nombre
        self.__edad = 0         # atributo privado para la edad
        self.__telefonos = []   # atributo privado para almacenar los teléfonos

    # -------- SETTERS (para modificar los atributos) --------
    def setNombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def setEdad(self, nueva_edad):
        self.__edad = nueva_edad

    def agregarTelefono(self, telefono):
        if telefono not in self.__telefonos:
            self.__telefonos.append(telefono)

    # -------- GETTERS (para acceder a los atributos) --------
    def getNombre(self):
        return self.__nombre

    def getEdad(self):
        return self.__edad

    def getTelefonos(self):
        return self.__telefonos

    # Método para mostrar toda la información del cliente
    def mostrar_info(self):
        print(f"Nombre: {self.getNombre()}")
        print(f"Edad: {self.getEdad()}")
        print("Teléfonos registrados:")
        for tel in self.getTelefonos():
            print(f" - {tel}")


# ----------- BLOQUE PRINCIPAL DEL PROGRAMA -----------

# Crear un nuevo cliente
cliente1 = Cliente()

# Asignar datos usando los setters
cliente1.setNombre("Gustavo Delnardo")
cliente1.setEdad(35)
cliente1.agregarTelefono("654321098")
cliente1.agregarTelefono("600123456")

# Mostrar la información del cliente
cliente1.mostrar_info()


#con este ejercicio aprendimos a crear y usar propiedades para acceder y modificar atributos privados de forma controlada. Vimos también cómo mantener una estructura limpia dentro de la clase usando getters y setters. Este enfoque resulta esencial para proteger los datos en sistemas como tiendas virtuales o videojuegos donde hay múltiples usuarios.
