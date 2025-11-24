#¡ADIVINA! v0.1
#Gustavo Delnardo
#Juego simple donde el usuario intenta adivinar un número secreto entre 1 y 50 con un maximo de 6 intentos.

'''
Aprendemos a usar bucles while para repetir intentos, condicionales if/elif/else para comparar números, try/except para manejar errores en las entradas y aserciones para asegurar que el número secreto y el contador de intentos estén dentro de los valores correctos.
Este ejercicio nos ayuda a practicar la lógica de programación básica y cómo controlar errores mientras interactuamos con el usuario.
'''

import random  # para generar el número secreto aleatoriamente

#Generamos el número secreto entre 1 y 50
numero_secreto = random.randint(1, 50)

#Aserción para asegurar que el número secreto está dentro del rango
assert 1 <= numero_secreto <= 50, "El número secreto está fuera del rango permitido."

# Inicializamos variables
intentos = 0
max_intentos = 6
acertado = False

# Bucle principal del juego
while intentos < max_intentos:
    try:
        # Pedimos el número al usuario
        entrada = input("Adivina un número entre 1 y 50: ")
        numero = int(entrada)  # Convertimos la entrada a entero
    except ValueError:
        print("Entrada no válida. Escribe un número entero.")
        continue  # No cuenta como intento, vuelve a pedir

    # Comprobamos que el número esté en el rango correcto
    if numero < 1 or numero > 50:
        print("El número debe estar entre 1 y 50.")
        continue  # Tampoco cuenta como intento

    # Sumamos el intento válido
    intentos += 1

    # Aserción para asegurar que el contador no sea negativo
    assert intentos >= 0, "El contador de intentos no puede ser negativo."

    # Comparamos el número con el secreto
    if numero == numero_secreto:
        print(f"¡HELL YEAH! ¡Has acertado el número secreto en {intentos} intento(s)!")
        acertado = True
        break
    elif numero < numero_secreto:
        print("El número es demasiado bajo.")
    else:
        print("El número es demasiado alto.")

    # A la tercera oportunidad, damos una pista de paridad
    if intentos == 3 and not acertado:
        if numero_secreto % 2 == 0:
            print("Pista: El número secreto es PAR.")
        else:
            print("Pista: El número secreto es IMPAR.")

# Al finalizar el juego
if not acertado:
    print("¡JA-JA! Se acabaron los intentos.")
    print(f"El número secreto era: {numero_secreto}")

#Con este juego comprendemos cómo se puede combinar repetición, selección y manejo de errores en un programa sencillo. Vemos la importancia de validar los datos del usuario y usar aserciones para que el programa funcione de manera segura. Este tipo de ejercicios es útil para aprender a construir juegos simples y mejorar la capacidad de depuración y control de la lógica en Python.
