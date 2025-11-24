En la programación, la depuración consiste en detectar y corregir errores que pueden aparecer durante la ejecución de un programa.
En este ejercicio, aprenderemos a crear una función llamada raizSegura() que calcule la raíz cuadrada de un número de manera controlada, utilizando estructuras de control, manejo de excepciones y aserciones.

Las aserciones sirven para comprobar si la función devuelve los resultados esperados con diferentes tipos de datos, y el bloque try/except se usa para evitar que el programa se bloquee cuando ocurre un error (por ejemplo, si el usuario introduce un texto en lugar de un número).

Este tipo de validación es muy importante en los videojuegos, donde las operaciones matemáticas deben ser seguras para que el juego no se detenga si se produce un valor inesperado.


Definición de la función
Se define una función llamada raizSegura(numero) que recibirá un valor como parámetro.
Esta función se encargará de devolver la raíz cuadrada si el número es válido o 0 si ocurre algún problema.

Validación del tipo de dato

Si el valor recibido es numérico (int o float) y mayor o igual a 0, se calcula su raíz cuadrada.

Si el valor recibido es una cadena que se puede convertir a número, se intenta convertir con float() y luego se calcula la raíz.

Si la conversión falla o si el número es negativo, la función devuelve 0.


Manejo de errores (try/except)
Se utiliza un bloque try/except para evitar que el programa se detenga si ocurre un error durante la conversión o el cálculo.
Esto garantiza que el programa siga funcionando de forma segura.

Comprobación con aserciones (assert)
Después de definir la función, se utilizan aserciones para comprobar si los resultados son correctos:

Que la raíz cuadrada de 9 sea 3.

Que la raíz cuadrada de un número negativo devuelva 0.

Que una cadena como "25" se convierta correctamente y devuelva 5.

Que una cadena no numérica devuelva 0.


Se probará la función con diferentes tipos de entrada para comprobar que funciona correctamente:

Un número entero positivo.

Un número negativo.

Una cadena que contiene un número.

Una cadena con texto.

Cada prueba mostrará si la función está manejando correctamente los errores y validaciones.


Este ejercicio muestra cómo probar y depurar funciones de manera segura, evitando errores que podrían detener el programa.
La función raizSegura() es un ejemplo claro de cómo aplicar buenas prácticas de programación:

Validar entradas,

Manejar errores con try/except,

Verificar resultados con assert,

Y documentar el código de forma clara.

En el contexto de los videojuegos, este tipo de comprobaciones es fundamental para evitar que el juego falle si el jugador introduce valores inesperados, manteniendo así la estabilidad y confiabilidad de la aplicación.


