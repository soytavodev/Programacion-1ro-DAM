'''
Programa: Gestor CRUD v1.0

Gustavo Delnardo
Descripción: Aplicación de consola en Python que permite gestionar una base de datos MySQL mediante operaciones CRUD (Crear, Leer, Actualizar, Eliminar). Incluye un menú interactivo con bucle infinito y captura de opciones del usuario.
'''

import mysql.connector

# ---------------------------------------------------------
# CONEXIÓN A LA BASE DE DATOS
# ---------------------------------------------------------
try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="tavo",          #cambia si usas otro usuario
        password="Hakaishin2.",          #agrega tu contraseña
        database="clientesdb", #usa la misma base de datos
        ssl_disabled=True,
        auth_plugin='mysql_native_password'
    )
    cursor = conexion.cursor()
except mysql.connector.Error as err:
    print("Error al conectar con la base de datos:", err)
    exit()

# ---------------------------------------------------------
# FUNCIÓN: INSERTAR CLIENTE
# ---------------------------------------------------------
def insertar_cliente():
    print("\n=== INSERTAR CLIENTE ===")
    dni = input("Introduce el DNI/NIE: ")
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")

    sql = "INSERT INTO clientes (dni, nombre, apellidos, email) VALUES (%s, %s, %s, %s)"
    valores = (dni, nombre, apellidos, email)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Cliente insertado correctamente.")

# ---------------------------------------------------------
# FUNCIÓN: LISTAR CLIENTES
# ---------------------------------------------------------
def listar_clientes():
    print("\n=== LISTADO DE CLIENTES ===")
    cursor.execute("SELECT * FROM clientes;")
    filas = cursor.fetchall()

    if not filas:
        print("No hay clientes registrados.")
    else:
        for fila in filas:
            print(f"ID: {fila[0]} | DNI: {fila[1]} | Nombre: {fila[2]} | Apellidos: {fila[3]} | Email: {fila[4]}")

# ---------------------------------------------------------
# FUNCIÓN: ACTUALIZAR CLIENTE
# ---------------------------------------------------------
def actualizar_cliente():
    print("\n=== ACTUALIZAR CLIENTE ===")
    id_cliente = input("Introduce el ID del cliente a actualizar: ")
    nuevo_nombre = input("Nuevo nombre: ")
    nuevos_apellidos = input("Nuevos apellidos: ")
    nuevo_email = input("Nuevo email: ")

    sql = "UPDATE clientes SET nombre=%s, apellidos=%s, email=%s WHERE id=%s"
    valores = (nuevo_nombre, nuevos_apellidos, nuevo_email, id_cliente)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Cliente actualizado correctamente.")

# ---------------------------------------------------------
# FUNCIÓN: ELIMINAR CLIENTE
# ---------------------------------------------------------
def eliminar_cliente():
    print("\n=== ELIMINAR CLIENTE ===")
    id_cliente = input("Introduce el ID del cliente a eliminar: ")
    confirmacion = input("¿Seguro que deseas eliminarlo? (S/N): ").lower()

    if confirmacion == "s":
        sql = "DELETE FROM clientes WHERE id=%s"
        cursor.execute(sql, (id_cliente,))
        conexion.commit()
        print("Cliente eliminado correctamente.")
    else:
        print("Operación cancelada.")

# ---------------------------------------------------------
# MENÚ PRINCIPAL
# ---------------------------------------------------------
while True:
    print("""
--------------------------------------------
Bienvenido al Gestor de Clientes
--------------------------------------------
1. Insertar cliente
2. Listar clientes
3. Actualizar cliente
4. Eliminar cliente
5. Salir
--------------------------------------------
""")

    opcion = input("Elige una opción (1-5): ")

    if opcion == "1":
        insertar_cliente()
    elif opcion == "2":
        listar_clientes()
    elif opcion == "3":
        actualizar_cliente()
    elif opcion == "4":
        eliminar_cliente()
    elif opcion == "5":
        print("Gracias por usar el Gestor de Clientes. ¡Hasta pronto!")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")

# ---------------------------------------------------------
# CIERRE DE CONEXIÓN
# ---------------------------------------------------------
conexion.close()


#Este simulacro integra todos los conceptos fundamentales de Python y MySQL vistos en clase: conexión a bases de datos, estructuras de control, bucles, entrada por teclado y operaciones CRUD. Representa la base de cualquier aplicación de gestión real, combinando la lógica de programación con el manejo de información persistente.
