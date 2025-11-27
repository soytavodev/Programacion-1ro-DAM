import random

patron = {1,2,3,4,5,6,7,8,9}

while True:
	lista = []
	for i in range(1,10):
		lista.append(random.randint(1,9))
	conjunto = set(lista)
	if conjunto == patron:
		print("El conjunto es correcto")
		print(conjunto)
		print(lista)
		#ahora elimino un numero
		indice = random.randint(1,9)
		lista[indice] = "_" #escoje un indice al azar y reemplaza su valor
		print(lista)
		break #fuerzo la finalizacion del bucle infinito

