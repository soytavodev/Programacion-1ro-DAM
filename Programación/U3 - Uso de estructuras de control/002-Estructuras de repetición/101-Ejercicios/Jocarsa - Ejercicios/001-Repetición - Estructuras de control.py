'''
Programa: Conteo de días pares y música v.01
Autor: Gustavo Delnardo - 1º DAM

Los videojuegos y la música forman parte del entretenimiento diario de las personas, demostraremos como la programación puede integrar estos dos elementos.

Nuestro objetivo es demostrar como podemos contar los dias pares del mes dentro de un rango o contar del 1 al 100 combinando con una lista de canciones que se reproducirán por cada dia que pasa. Practicaremos la utilizacion de variables, bucles for, iteración con rangos, operadores y listas. Asi comprendemos cómo la programación puede mezclar la lógica con el entretenimiento, reforzando la comprensión de los bucles en Python.
'''

#declaramos variables:

#contador inicializa en cero.
contador = 0 

#creamos la lista de canciones que se van a reproducir.
canciones = ["CDC - Rubia sol, morena luna",
"Blink-182 - One more time",
"Nightwish - Dark chest of wonders",
"Slipknot - Duality"
]

#recorremos los dias pares del mes.
for dia in range(2,31,2):
	cancion = canciones[contador % len (canciones)] #calcula la cancion para ese dia y utilizamos el operador módulo para rotar entre los elementos de la lista de canciones.
	print("Hoy es el dia",dia,"del mes. Reproduciendo:",cancion)
	contador += 1 #El contador aumentará en uno por cada dia que pasa.
	
print("Total de dias pares contados:",contador)

#Con éste ejercicio comprendemos como funcionan los bucles, las listas, las iteraciones y el operador modulo. la importancia de éstas estructuras radican en que nos permiten automatizar actividades repetitivas en menos lineas de código. Éste tipo de estructuras pueden aplicarse en videojuegos, por ejemplo, para controlar ciclos como el conteo de vidas, el avance de niveles o el reinicio del juego cuando el personaje pierde toda su energía.
