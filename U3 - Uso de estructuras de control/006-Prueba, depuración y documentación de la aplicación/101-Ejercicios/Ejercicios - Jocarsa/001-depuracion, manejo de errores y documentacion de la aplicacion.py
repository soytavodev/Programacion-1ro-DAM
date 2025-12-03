# raiz_segura.py v.01
# Autor: Gustavo Delnardo
#Prueba, depuración y documentación de la aplicación

# En este programa vamos a crear una función llamada raizSegura que calcule la raíz cuadrada de un número, pero de forma segura. Esto significa que no debe dar error si el dato no es un número o si es negativo.

def raizSegura(numero):
    """
    Función que calcula la raíz cuadrada de un número de forma segura.
    Si el número es válido y positivo, devuelve su raíz cuadrada.
    Si no, devuelve 0.
    """
    try:
        # Intentamos convertir el valor a número flotante
        num = float(numero)
        
        # Si el número es negativo, devolvemos 0
        if num < 0:
            return 0
        
        # Si todo está bien, devolvemos su raíz cuadrada
        resultado = num ** 0.5
        return resultado

    except:
        # Si algo falla (por ejemplo, si se pone texto), devolvemos 0
        return 0


# Pruebas con diferentes valores
print("Pruebas de la función raizSegura:")

# Casos de prueba
print("Raíz de 9 =", raizSegura(9))          # debería dar 3
print("Raíz de -4 =", raizSegura(-4))        # debería dar 0
print("Raíz de '25' =", raizSegura("25"))    # debería dar 5
print("Raíz de 'hola' =", raizSegura("hola"))# debería dar 0

# Ahora probamos con aserciones para comprobar que la función funciona bien
# Las aserciones son pruebas que nos dicen si algo no está funcionando como debería

assert raizSegura(9) == 3, "Error: la raíz de 9 no es 3"
assert raizSegura(-4) == 0, "Error: los números negativos deben devolver 0"
assert raizSegura("25") == 5, "Error: la cadena '25' no devuelve 5"
assert raizSegura("hola") == 0, "Error: una palabra debe devolver 0"

print("Todas las pruebas pasaron correctamente :)")

