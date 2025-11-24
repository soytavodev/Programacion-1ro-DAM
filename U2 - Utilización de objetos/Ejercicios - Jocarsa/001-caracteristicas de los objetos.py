'''
Programa: Características de los Objetos v0.1

Autor: Gustavo Delnardo - 1º DAM

En los videojuegos, muchas veces necesitamos hacer cálculos matemáticos para controlar elementos del juego, como la posición de los personajes, su velocidad o el tamaño de objetos. Python nos proporciona objetos predefinidos que nos facilitan estas operaciones. En este ejercicio veremos cómo usar algunos de ellos para cálculos básicos como raíces cuadradas, números aleatorios y áreas de círculos.
'''

#Importamos los módulos necesarios

import math   # Módulo para operaciones matemáticas
import random # Módulo para generar números aleatorios

#Calculamos la raíz cuadrada de un número

numero = 49
raiz = math.sqrt(numero)  # Usamos sqrt del módulo math
print("La raíz cuadrada de", numero, "es:", raiz)

#Generaramos un número aleatorio entre 1 y 100

aleatorio = random.randint(1, 100)  # randint del módulo random
print("Número aleatorio generado:", aleatorio)


#Calculamos el área de un círculo

radio = 5  # Podríamos pedirlo al usuario, aquí usamos un valor fijo
area = math.pi * (radio ** 2)  # Área = pi * r^2
print("El área de un círculo de radio", radio, "es:", area)


#Con este ejercicio aprendimos a usar objetos predefinidos en Python como math y random. Estas herramientas nos permiten hacer cálculos matemáticos y generar números aleatorios de manera fácil, algo que es muy útil en videojuegos. Por ejemplo, podríamos calcular distancias, áreas de objetos, o decidir acciones aleatorias de enemigos en un juego. Usar objetos predefinidos ayuda a que nuestro código sea más limpio y no tengamos que escribir funciones complicadas desde cero.
