'''
Programa: Gestión de Clientes v0.1

Gustavo Delnardo

Vamos a crear un sistema interactivo de gestión de clientes relacionado con tus hobbies: videojuegos y música. Aprenderemos a insertar, listar, actualizar y eliminar clientes usando clases y menús en Python.
Este ejercicio nos enseña cómo manejar datos de manera organizada, como en cualquier plataforma de juegos o música.
'''

#definición de la clase Cliente
class Cliente:
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

#lista donde almacenaremos los clientes
clientes = []

#menú principal
while True:
    print("\n###### Gestión de clientes v0.1 ######")
    print("####### Gustavo Delnardo #######")
    print("Escoge una opción:")
    print("1.-Insertar un cliente")
    print("2.-Listar clientes")
    print("3.-Actualizar un cliente")
    print("4.-Eliminar un cliente")
    print("5.-Salir")
    
    opcion = input("Escoge una opción: ").strip()
    
    if opcion == "1":
        #insertar cliente
        nombre = input("Introduce el nombre: ").strip()
        apellidos = input("Introduce los apellidos: ").strip()
        email = input("Introduce el email: ").strip()
        nuevo_cliente = Cliente(nombre, apellidos, email)
        clientes.append(nuevo_cliente)
        print("Cliente insertado correctamente.")
        
    elif opcion == "2":
        #listar clientes
        if len(clientes) == 0:
            print("No hay clientes en la lista.")
        else:
            for idx, cliente in enumerate(clientes):
                print(f"\nEste es el cliente con ID: {idx}")
                print(f"{cliente.nombre} {cliente.apellidos} {cliente.email}")
    
    elif opcion == "3":
        #actualizar cliente
        if len(clientes) == 0:
            print("No hay clientes para actualizar.")
        else:
            id_actualizar = int(input("Introduce el ID del cliente a actualizar: "))
            if 0 <= id_actualizar < len(clientes):
                cliente = clientes[id_actualizar]
                cliente.nombre = input("Nuevo nombre: ").strip()
                cliente.apellidos = input("Nuevos apellidos: ").strip()
                cliente.email = input("Nuevo email: ").strip()
                print("Cliente actualizado correctamente.")
            else:
                print("ID no válido.")
                
    elif opcion == "4":
        #eliminar cliente
        if len(clientes) == 0:
            print("No hay clientes para eliminar.")
        else:
            id_eliminar = int(input("Introduce el ID del cliente a eliminar: "))
            if 0 <= id_eliminar < len(clientes):
                confirmacion = input("¿Estás seguro que deseas eliminar este cliente? (S/N): ").strip().lower()
                if confirmacion == "s":
                    clientes.pop(id_eliminar)
                    print("Cliente eliminado correctamente.")
                else:
                    print("Operación cancelada.")
            else:
                print("ID no válido.")
                
    elif opcion == "5":
        #salir del programa
        print("Saliendo del programa...")
        break
        
    else:
        print("Opción no válida. Intenta de nuevo.")


#Con este ejercicio aprendimos a gestionar datos de clientes usando clases y menús en Python. Vimos cómo realizar operaciones CRUD básicas (Crear, Leer, Actualizar, Eliminar) de forma segura. Estas técnicas son aplicables a sistemas de gestión de usuarios en videojuegos, música o cualquier aplicación real.
