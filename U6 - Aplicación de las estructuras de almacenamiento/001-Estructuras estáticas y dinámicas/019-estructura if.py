print("Lista de la compra v0.1")

while True:
	print("Selecciona una opción")
	print("1.-Añadir elemento a la lista")
	print("2.-Leer la lista")
	opcion = int(input("Tu opción: "))
	
	if opcion == 1:
		print("Añadimos un elemnto a la lista:")
		nombre = input("Indica el nombre del producto: ")
		cantidad =input("Indica la cantidad del producto: ")
	elif opcion == 2:
