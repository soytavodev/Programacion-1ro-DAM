'''
Métodos Estáticos en videojuegos v0.1


Gustavo Delnardo

Un método estático es una función que pertenece a una clase pero no necesita una instancia (un objeto) para ser utilizada. En este ejercicio aprendemos a usar un método estático, que es una función que pertenece a la clase pero no necesita un objeto específico para trabajar. Esto sirve en videojuegos cuando necesitamos calcular algo como daño o estadísticas sin depender de un personaje concreto.


Ejemplo:
'''

#creamos un objeto Personaje como un diccionario, aunque normalmente sería una clase
Personaje = {
    "nombre": "Gandalf",
    "nivel": 10,
    "vida": 100
}

#método estático simulado como función independiente
def calcularDaño(nivel):
    """Calcula el daño basado en el nivel del personaje"""
    daño = nivel * 2  # cada nivel da 2 puntos de daño
    return daño

#usamos el método estático para calcular el daño del personaje
daño_gandalf = calcularDaño(Personaje["nivel"])
print(f"El personaje {Personaje['nombre']} hace {daño_gandalf} puntos de daño")

#aprendi que los métodos estáticos nos permiten hacer cálculos útiles sin depender de un objeto específico, por ejemplo para estadísticas globales de un juego.
