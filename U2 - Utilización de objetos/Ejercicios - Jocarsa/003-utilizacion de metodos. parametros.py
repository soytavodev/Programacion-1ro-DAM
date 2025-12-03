"""
¡Calcular Puntuación de Juego! v0.1
Gustavo Delnardo
Este programa calcula la puntuación de un jugador basado en el tiempo que jugó.
"""

import math  #importamos math para usar ceil

#función para calcular la puntuación
def calcular_puntuacion(tiempo_juego):
    """
    Calcula la puntuación de un jugador según el tiempo jugado.
    Redondea el tiempo hacia arriba y multiplica por 10.
    """
    #redondeamos hacia arriba el tiempo
    tiempo_redondeado = math.ceil(tiempo_juego)
    
    #calculamos la puntuación final
    puntuacion = tiempo_redondeado * 10
    
    return puntuacion  # devolvemos la puntuación

#ejemplo de uso
tiempo = 7.2  #tiempo que jugó el jugador en minutos
puntaje = calcular_puntuacion(tiempo)
print("Tiempo jugado:", tiempo, "minutos")
print("Puntuación final:", puntaje, "puntos")

