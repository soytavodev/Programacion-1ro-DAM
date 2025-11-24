"""
Calculadora de Cuadras con Música
Gustavo Delnardo
En este ejercicio vamos a crear una calculadora para saber cuántas cuadras necesito si tengo varios caballos en mi juego favorito "Música en Las Cuadras". La idea es que, además de calcular, el programa pueda poner un poco de música divertida mientras se muestran los resultados. Esto me ayuda a practicar cómo usar entradas de usuario, cálculos simples y mostrar resultados en Python, y también a experimentar con cómo podemos usar objetos externos como los de pygame para reproducir sonidos.
"""

#importamos pygame para reproducir música
import pygame
import math #esto para redondear hacia arriba

#datos iniciales
caballos = 0
cuadras_por_caballo = 0

#entrada de información
caballos = int(input("Introduce el número de caballos: "))
cuadras_por_caballo = int(input("Introduce cuántos caballos pueden alojarse en cada cuadra: "))

#realización de cálculos
#usamos math.ceil() para que redondee hacia arriba (ej: 3.33 -> 4)
cuadras_necesarias = math.ceil(caballos / cuadras_por_caballo)

#salida de resultados
print("Si tienes", caballos, "caballos")
print("Y se pueden alojar", cuadras_por_caballo, "caballos por cuadra")
# Ya no necesitamos round(), porque math.ceil() nos da el número entero correcto
print("En ese caso necesitas", cuadras_necesarias, "cuadras")

#reproducción de música
pygame.init() #inicializamos pygame

#nos aseguramos de tener el archivo 'musica_divertida.mp3' en la misma carpeta
pygame.mixer.music.load('musica_divertida.mp3') # Cargamos la música
pygame.mixer.music.play() # La reproducimos

#esperamos un poco para que se escuche la música (opcional)
input("Presiona Enter para terminar el programa y detener la música...")
pygame.mixer.music.stop()


#este ejercicio refuerza la importancia de las estructuras de entrada, cálculo y salida, y cómo los objetos preexistentes nos ayudan a realizar tareas sin complicarnos con cosas avanzadas. En el futuro, estos conceptos se pueden aplicar para crear mini juegos o herramientas interactivas más complejas.



