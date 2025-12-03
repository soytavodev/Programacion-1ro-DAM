'''
MusicWeb Client Manager v0.1

Gustavo Delnardo

Descripción: Gestión de información de clientes usando métodos (setters y getters) en Python.
'''

#definición de la clase Cliente
class Cliente:
    #método constructor
    def __init__(self):
        self.__nombrecompleto = ""  #atributo privado para el nombre completo
        self.__email = ""            #atributo privado para el email

    # -------- MÉTODOS (SETTERS Y GETTERS) --------

    #setter para cambiar el nombre completo del cliente
    def setNombreCompleto(self, nuevonombre):
        self.__nombrecompleto = nuevonombre

    #getter para obtener el email del cliente
    def getEmail(self):
        return self.__email

    #setter opcional para establecer el email
    def setEmail(self, nuevoemail):
        self.__email = nuevoemail

    #método para mostrar toda la información del cliente
    def mostrar_info(self):
        print("Nombre completo:", self.__nombrecompleto)
        print("Email:", self.__email)


# ----------- BLOQUE PRINCIPAL DEL PROGRAMA -----------

#crear una instancia de Cliente
cliente1 = Cliente()

#usar métodos para establecer valores
cliente1.setNombreCompleto("Gustavo Delnardo")
cliente1.setEmail("gustavo1@gmail.com")

#mostrar la información usando los atributos privados a través de los métodos
cliente1.mostrar_info()


#Con este ejercicio comprendimos cómo definir métodos dentro de una clase para controlar el acceso a los atributos privados. Aprendimos a usar setters para modificar y getters para leer la información de forma segura. Estos conceptos son esenciales para gestionar datos de clientes en aplicaciones reales, como tiendas de música o videojuegos online.
