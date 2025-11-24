'''
Creador de Agenda v0.1

Gustavo Delnardo

Vamos a añadir y leer contactos usando archivos de texto en Python. En este ejercicio aprenderemos a usar archivos de texto para almacenar y leer contactos de manera sencilla. Simularemos una agenda digital donde podemos guardar nombres y emails de amigos o familiares. Esto nos permite practicar flujos de entrada y salida y la interacción con el usuario.
'''

# ----------- BLOQUE PRINCIPAL DEL PROGRAMA -----------

#menú de opciones
while True:
    print("\nSelecciona una opción:")
    print("1.-Introduce un nuevo contacto")
    print("2.-Leer todos los contactos")
    print("3.-Salir")

    opcion = input("Indica tu opción (1,2,3): ")

    if opcion == "1":
        #abrimos el archivo en modo 'a' (append) para añadir datos al final
        archivo = open("agenda.txt", "a", encoding="utf-8")

        #pedimos los datos al usuario
        nombre = input("Introduce el nombre del contacto: ")
        email = input("Introduce el email del contacto: ")

        #escribimos los datos en el archivo
        archivo.write("Nombre: " + nombre + "\n")
        archivo.write("Email: " + email + "\n")
        archivo.write("--------------------\n")  # Separador entre contactos

        #cerramos el archivo
        archivo.close()
        print("Contacto añadido correctamente.")

    elif opcion == "2":
        #abrimos el archivo en modo lectura
        try:
            archivo = open("agenda.txt", "r", encoding="utf-8")
            contenido = archivo.read()  # Leemos todo el contenido
            print("\n--- Contactos en la agenda ---")
            print(contenido)
            archivo.close()  # Cerramos el archivo
        except FileNotFoundError:
            print("No hay contactos todavía. Añade uno primero.")

    elif opcion == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")

#Con este ejercicio aprendimos a usar archivos de texto para almacenar información de manera persistente. Vimos cómo abrir, escribir y leer archivos y cómo gestionar los flujos correctamente. Esto es útil para crear agendas, listas de usuarios o cualquier tipo de datos que necesitemos guardar entre ejecuciones del programa.
