'''
Programa: Comprobación de edad con aserciones v0.1
Autor: Gustavo Delnardo

Las aserciones en programación sirven para comprobar si algo en el programa se está cumpliendo como debería. 
Son como una pequeña verificación que nos dice si los valores son correctos o no. 
Esto es muy útil cuando queremos asegurarnos de que una variable tiene el valor esperado antes de continuar la ejecución del programa. 

Por ejemplo, en los videojuegos, las aserciones podrían servir para comprobar si la puntuación o la vida del jugador están dentro de un rango válido.
'''

# Declaramos una variable con un valor fijo.
edad = 47

try:
    # Comprobamos si la edad es la esperada (48).
    # Si no lo es, mostrará el mensaje definido en el assert.
    assert edad == 48, "no es correcto"

    # Si la comprobación es verdadera, se mostrará este mensaje.
    print("La comprobación fue exitosa. La edad es correcta.")

except AssertionError as e:
    # Si la aserción falla, se captura el error y se muestra un mensaje.
    print("Error determinado:", e)

# Probando con otro valor
# Si cambiamos edad = 48, no aparecerá el error.
# Si lo dejamos en 47, se activará el mensaje de error.

#En conclusión, las aserciones nos ayudan a comprobar rápidamente si una parte del programa funciona como esperamos. Aunque parecen simples, son muy útiles porque evitan que el programa siga ejecutándose con valores incorrectos. En un videojuego, por ejemplo, podríamos usar aserciones para verificar que la vida del jugador nunca sea negativa o que el nivel actual exista. De esta forma, hacemos que el código sea más seguro y fácil de depurar.
