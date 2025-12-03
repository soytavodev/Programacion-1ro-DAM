# ---------- Duelo Relámpago ----------

edad_mago = input("Dime la edad del mago: ")

try:
    edad_mago = int(edad_mago)
except ValueError:
    edad_mago = 100

# Clasificación del mago según su edad
if edad_mago < 30:
    clasificacion_mago = "Aprendiz"
elif edad_mago <= 99:
    clasificacion_mago = "Hechicero"
else:
    clasificacion_mago = "Archimago"

# Función que devuelve el poder base del mago según su clasificación
def poderBase(edad):
    """Devuelve el poder base del mago según su edad."""
    if edad < 30:
        return 5
    elif edad <= 99:
        return 8
    else:
        return 10

poder_base = poderBase(edad_mago)

print("\n--- Información del Mago ---")
print(f"Mago: {clasificacion_mago}, Edad: {edad_mago}, Poder Base: {poder_base}")
