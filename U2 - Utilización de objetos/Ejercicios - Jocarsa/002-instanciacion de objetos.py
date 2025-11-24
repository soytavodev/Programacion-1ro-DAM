"""
Cálculo de estadísticas musicales v0.1
Gustavo Delnardo
Este programa calcula cosas sencillas sobre mis canciones favoritas.
"""

import statistics  # Esto sirve para calcular el promedio de números

# Lista de canciones: cada canción tiene nombre, duración y género
canciones = [
    {"nombre": "Rubia sol, morena luna", "duracion": 3.5, "genero": "Pop"},
    {"nombre": "One more time", "duracion": 4.2, "genero": "Rock"},
    {"nombre": "Dark chest of wonders", "duracion": 5.1, "genero": "Metal"},
    {"nombre": "Duality", "duracion": 4.0, "genero": "Metal"}
]

# Guardamos todas las duraciones en una lista
duraciones = []
for cancion in canciones:
    duraciones.append(cancion["duracion"])  # vamos metiendo cada duración

# Calculamos el promedio
promedio = statistics.mean(duraciones)
print("El promedio de duración de las canciones es:", promedio, "minutos")

# Contamos cuántas canciones hay por cada género
conteo_genero = {}
for cancion in canciones:
    genero = cancion["genero"]
    if genero in conteo_genero:
        conteo_genero[genero] += 1
    else:
        conteo_genero[genero] = 1

print("Cantidad de canciones por género:")
for genero, cantidad in conteo_genero.items():
    print(genero + ":", cantidad)

#aprendí a usar listas y diccionarios para guardar info de canciones.
#esto ayuda a hacer cuentas automáticamente y también podría usarlo
#para cosas de videojuegos, como llevar el registro de puntos o personajes.

