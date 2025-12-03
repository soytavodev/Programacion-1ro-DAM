# Programa: Manejo de Errores y con try-except v0.1
# Autor: Gustavo Delnardo

'''
En Python, el try-except se usa para manejar errores que pueden aparecer mientras el programa se está ejecutando. A veces al hacer una operación, como dividir entre cero o acceder a un elemento que no existe en una lista, el programa se detiene y muestra un error.
Con try-except, el programa puede “atrapar” esos errores y seguir funcionando sin que se cierre por completo.

Esto es muy útil, sobre todo en los videojuegos o programas grandes, donde pueden pasar muchas cosas a la vez y es importante que el programa no se detenga por un solo fallo. En este ejercicio aprenderemos a manejar diferentes tipos de errores y a crear una función que también use este control.
'''

#error.py
#Este programa intenta dividir entre cero, lo que genera un error.
numero = 10
resultado = numero / 0
print("El resultado es:", resultado)

#Al ejecutarlo, el programa se detiene y muestra un error porque no se puede dividir entre cero. Para evitar que se detenga, usamos try-except en un nuevo archivo llamado manejo_errores.py:

#Aquí controlamos el error de división entre cero.

try:
    numero = 10
    resultado = numero / 0
    print("El resultado es:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
    
#Después, añadimos otro tipo de error, como intentar acceder a una posición que no existe en una lista:

try:
    lista = [1, 2, 3]
    print(lista[5])  # Este índice no existe
except IndexError:
    print("Error: El índice de la lista no existe.")

#Ahora creamos una función que también use el manejo de errores:

# Función para calcular una potencia
def calcular_potencia(base, exponente):
    try:
        # Intentamos calcular la potencia
        resultado = base ** exponente
        return resultado
    except TypeError:
        print("Error: Los valores deben ser numéricos.")
    except Exception as e:
        print("Ha ocurrido un error:", e)

# Llamadas de ejemplo
print(calcular_potencia(2, 3))
print(calcular_potencia(-2, "a"))

#El uso de try-except nos permite manejar los errores de forma controlada y seguir ejecutando el programa sin que se cierre de golpe. Esto es muy importante en la programación real, por ejemplo, en un videojuego, donde pueden aparecer muchos errores por acciones inesperadas del jugador. Aprender a controlar los errores hace que el programa sea más estable y profesional.



