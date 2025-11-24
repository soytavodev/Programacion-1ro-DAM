print("Inventario de pociones v0.1")
import json #para usar la libreria tengo que importarla

inventario_de_pociones = []

while True:
	print("Selecciona una opción")
	print("1.-Añadir poción a la lista")
	print("2.-Leer la lista de pociones")
	opcion = int(input("Tu opción: "))
	
	if opcion == 1:
		print("Añadimos un elemento a la lista:")
		tipo = input("Indica el tipo de poción: ")
		cantidad =input("Indica la cantidad de pociones: ")
		inventario_de_pociones.append({"tipo":tipo,"cantidad":cantidad})
		archivo = open("lista.json","w")			#abro un archivo
		json.dump(inventario_de_pociones, archivo) #guardo en json
		archivo.close()												#cierro el archivo	
	elif opcion == 2:
		print("Listamos las pociones de la lista:")
		print (inventario_de_pociones)
		for tipo in inventario_de_pociones:
			print("Poción:",tipo['tipo'])
			print("Cantidad:",tipo['cantidad'])
			print("###############################") #esto es estético, es un separador
