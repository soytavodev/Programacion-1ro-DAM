import pickle
agenda = []

while True:
	print("Selecciona una opcion: ")
	print("1.-Insertar un registro")
	print("2.-Leer registros")
	print("3.-Guardar registro")
	print("4.-Eliminar registro")
	opcion = int(input("Opcion escogida: "))
	if opcion == 1:
		#insertar
		nombre = input("Dime tu nombre: ")
		apellidos = input("Dime tus apellidos: ")
		email = input("Dime tu email: ")
		telefono = input("Dime tu telefono: ")
		agenda.append([nombre,apellidos,email,telefono])
	elif opcion == 2:
		#imprimir
		print(agenda)
	elif opcion == 3:
		print("Registro guardado correctamente 🫰️")
		#guardar
		archivo = open("agenda.bin","wb")
		pickle.dump(agenda,archivo)
		archivo.close()
	elif opcion == 4:
	indice = int(input("Indica el número del registro a eliminar: "))

	if indice >= 0 and indice < len(agenda):
		agenda.pop(indice)
		print("Registro eliminado.")
	else:
		print("Error: índice fuera de rango.")

