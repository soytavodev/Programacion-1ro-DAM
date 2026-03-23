import time

inicio = time.time()

numero = 1.0000000432
contador = 0

for contador in range(235324544):  # en C el for es <=, así que +1
    numero = numero * 1.00000000645

fin = time.time()

tiempo = fin - inicio

print("El resultado es:", numero)
print("Tiempo de ejecución:", tiempo, "segundos")
