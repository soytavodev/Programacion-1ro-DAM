'''
En este programa vamos a registrar información sobre dos dragones, simular su entrenamiento
durante tres días y calcular el poder de un mago según su edad. Usamos try/except para manejar
errores de entrada, bucles for para entrenamientos y una función para calcular el poder base.
'''

# ---------- Registro de Dragones ----------

# Dragón A
nombre_dragon_a = input("Dime el nombre del dragón A: ")
edad_dragon_a = input("Dime la edad del dragón A: ")

try:
    edad_dragon_a = int(edad_dragon_a)  # Intentamos convertir a entero
except ValueError:
    edad_dragon_a = 100  # Si falla, asignamos 100 años por defecto

# Clasificación del Dragón A según edad
if edad_dragon_a < 50:
    clasificacion_dragon_a = "Joven"
elif edad_dragon_a <= 199:
    clasificacion_dragon_a = "Adulto"
else:
    clasificacion_dragon_a = "Anciano"

fuerza_dragon_a = 0  # Inicializamos la fuerza

# Dragón B
nombre_dragon_b = input("Dime el nombre del dragón B: ")
edad_dragon_b = input("Dime la edad del dragón B: ")

try:
    edad_dragon_b = int(edad_dragon_b)
except ValueError:
    edad_dragon_b = 100

if edad_dragon_b < 50:
    clasificacion_dragon_b = "Joven"
elif edad_dragon_b <= 199:
    clasificacion_dragon_b = "Adulto"
else:
    clasificacion_dragon_b = "Anciano"

fuerza_dragon_b = 0  # Inicializamos la fuerza

# ---------- Entrenamiento de Dragones ----------

# 3 días de entrenamiento para Dragón A
for dia in range(1, 4):
    if clasificacion_dragon_a == "Joven":
        fuerza_dragon_a += 2
    else:
        fuerza_dragon_a += 1

# 3 días de entrenamiento para Dragón B
for dia in range(1, 4):
    if clasificacion_dragon_b == "Joven":
        fuerza_dragon_b += 2
    else:
        fuerza_dragon_b += 1
        
print("\n--- Información de los Dragones ---")
print(f"Dragón A: {nombre_dragon_a}, Edad: {edad_dragon_a}, Clasificación: {clasificacion_dragon_a}, Fuerza: {fuerza_dragon_a}")
print(f"Dragón B: {nombre_dragon_b}, Edad: {edad_dragon_b}, Clasificación: {clasificacion_dragon_b}, Fuerza: {fuerza_dragon_b}")
