# planificador_cuadras.py
# Autor: Gustavo Delnardo
# Calcula cuántas cuadras se necesitan para alojar a un número de caballos según su capacidad, mostrando además información sobre la fecha.

'''
El propósito de este ejercicio es practicar cómo pedir información al usuario usando la función input(). Luego, toma esa información (guardada en variables como caballos y capacidad) y la usa para hacer un cálculo matemático simple. Finalmente, muestra el resultado en pantalla.
'''

import math          # Para usar math.ceil
from datetime import date  # Para trabajar con fechas

# 1. ENTRADA DE DATOS
try:
    caballos = int(input("Ingrese el número de caballos: "))
    capacidad = int(input("Ingrese la capacidad por cuadra: "))
    fecha_str = input("Ingrese la fecha (formato YYYY-MM-DD): ")

    # Validación de valores positivos
    if caballos <= 0 or capacidad <= 0:
        print("Error: Los valores deben ser enteros positivos.")
        exit()

    # 2. CONVERSIÓN DE FECHA
    año, mes, dia = map(int, fecha_str.split("-"))
    fecha = date(año, mes, dia)

except ValueError:
    # Si ocurre un error al convertir números o fecha
    print("Error: Datos inválidos. Asegúrese de usar números enteros y el formato correcto de fecha (YYYY-MM-DD).")
    exit()

# 3. CÁLCULOS
cuadras_necesarias = math.ceil(caballos / capacidad)  # Redondea hacia arriba
weekday = fecha.weekday()       # Lunes=0 ... Domingo=6
isoweekday = fecha.isoweekday() # Lunes=1 ... Domingo=7

# 4. SALIDA DE RESULTADOS
print("\n--- INFORME DEL PLANIFICADOR DE CUADRAS ---")
print(f"Caballos: {caballos}")
print(f"Capacidad por cuadra: {capacidad}")
print(f"Cuadras necesarias (redondeadas al alza): {cuadras_necesarias}")

print("\n--- DATOS DE LA FECHA ---")
print(f"Fecha ingresada: {fecha}")
print(f"Año: {fecha.year}")
print(f"Mes: {fecha.month}")
print(f"Día: {fecha.day}")
print(f"weekday(): {weekday}")
print(f"isoweekday(): {isoweekday}")

# 5. VERIFICAR SI ES ENTRE SEMANA O EL FIN DE SEMANA
if isoweekday >= 6:
    print("La fecha cae en fin de semana.")
else:
    print("La fecha cae entre semana.")


'''
Como se puede ver, el programa sigue una secuencia lógica clara: Entrada, Proceso y Salida. Primero, recoge los datos. Segundo, procesa esos números (haciendo una división) y también revisa la fecha. Tercero, imprime un informe ordenado. Este ejercicio es una demostración perfecta de cómo se usan las variables para guardar datos, los operadores matemáticos para hacer cálculos, y la lógica if para tomar decisiones simples.
'''

