'''
Estructura de una clase

Gustavo Delnardo

Una clase se compone principalmente de tres tipos de miembros: Atributos, Metodos y Constructores.
En este ejercicio aplicamos el concepto de clases con atributos privados, simulando un escenario real de desarrollo de videojuegos.
'''

#definición de la clase Jugador
class Jugador:
    def __init__(self, nombre, email, nivel):
        # Atributos privados
        self.__nombre = nombre
        self.__email = email
        self.__nivel = nivel

    #método para mostrar la información del jugador
    def mostrar_info(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Email: {self.__email}")
        print(f"Nivel: {self.__nivel}")
        print("-" * 25)


#solicitud de datos para el jugador actual
nombre_usuario = input("Introduce tu nombre: ")
email_usuario = input("Introduce tu email: ")
nivel_usuario = input("Introduce tu nivel actual: ")

#creación de los objetos
jugador_actual = Jugador(nombre_usuario, email_usuario, nivel_usuario)
jugador_invitado = Jugador("Invitado", "invitado@game.com", "1")

#mostrar la información de ambos jugadores
print("\n--- Información de los jugadores ---")
jugador_actual.mostrar_info()
jugador_invitado.mostrar_info()


#Con este ejercicio aprendimos a estructurar una clase con atributos privados y un método para mostrar su información. También comprendimos la importancia de proteger los datos internos mediante visibilidad y usar el constructor para inicializarlos. Este enfoque es esencial en videojuegos o aplicaciones donde los datos del jugador deben gestionarse de forma controlada y segura.
