"""
Objetos y Propiedades v0.1
Gustavo Delnardo
Ejemplo sencillo de cómo usar propiedades en un objeto jugador. En este ejercicio aprendemos a usar las propiedades de un objeto para guardar información de un jugador, como su nombre, puntos, nivel y vida. Esto sirve en videojuegos para saber el estado de cada personaje sin tener que usar muchas variables separadas.

"""

#creamos un objeto Jugador como un diccionario
Jugador = {
    "nombre": "Gustavo",
    "puntos": 10,
    "nivel": 1,
    "vida": 100
}

#mostramos las propiedades del jugador
print("Nombre:", Jugador["nombre"])
print("Puntos:", Jugador["puntos"])
print("Nivel:", Jugador["nivel"])
print("Vida:", Jugador["vida"])

#modificamos la propiedad puntos
Jugador["puntos"] = 20
print("Puntos después de sumar:", Jugador["puntos"])

#añadimos un método para aumentar puntos
def aumentar_puntos(jugador, cantidad):
    jugador["puntos"] += cantidad  # sumamos los puntos
    return jugador["puntos"]

#usamos el método
nuevos_puntos = aumentar_puntos(Jugador, 5)
print("Puntos después de usar aumentar_puntos():", nuevos_puntos)

#Ahora sé cómo crear un objeto simple con propiedades y cómo acceder y modificar sus valores. También puedo añadir funciones que actúan sobre el objeto, como aumentar puntos. Esto me ayudará en futuros proyectos de juegos o cualquier programa donde necesite organizar datos de manera ordenada.


