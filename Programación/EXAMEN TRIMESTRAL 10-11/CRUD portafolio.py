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
        user="gustavo",          #cambia si usas otro usuario
        password="Hakaishin2.",          #agrega tu contraseña
        database="portafolioexamen", #usa la misma base de datos
    )
    cursor = conexion.cursor()
except mysql.connector.Error as err:
    print("Error al conectar con la base de datos:", err)
    exit()
    
# ---------------------------------------------------------
# FUNCIÓN: INSERTAR PIEZA
# ---------------------------------------------------------
def insertar_piezas():
    print("\n=== INSERTAR PIEZA ===")
    titulo = input("Introduce el titulo de la pieza: ")
    descripcion = input("Introduce la descripcion: ")
    fecha = input("Introduce la fecha: ")

    sql = "INSERT INTO piezasportafolio (titulo, descripcion, fecha) VALUES (%s, %s, %s)"
    valores = (titulo, descripcion, fecha)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Pieza insertada correctamente.")

# ---------------------------------------------------------
# FUNCIÓN: LISTAR PIEZAS
# ---------------------------------------------------------
def listar_piezas():
    print("\n=== LISTADO DE PIEZAS ===")
    cursor.execute("SELECT * FROM piezasportafolio;")
    filas = cursor.fetchall()

    if not filas:
        print("No hay piezas registradas.")
    else:
        for fila in filas:
            print(f"ID: {fila[0]} | Título: {fila[1]} | Descripción: {fila[2]} | Fecha: {fila[3]}")

# ---------------------------------------------------------
# FUNCIÓN: ACTUALIZAR PIEZAS
# ---------------------------------------------------------
def actualizar_piezas():
    print("\n=== ACTUALIZAR PIEZA ===")
    id_piezas = input("Introduce el ID de la pieza a actualizar: ")
    nuevo_nombre = input("Nuevo nombre de la pieza: ")
    nueva_descripcion = input("Nueva descripción de la pieza: ")
    nueva_fecha = input("Nueva fecha de la pieza: ")

    sql = "UPDATE piezasportafolio SET titulo=%s, descripcion=%s, fecha=%s WHERE id_categoria=%s"
    valores = (nuevo_nombre, nueva_descripcion, nueva_fecha, id_piezas)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Pieza actualizada correctamente.")

# ---------------------------------------------------------
# FUNCIÓN: ELIMINAR PIEZA
# ---------------------------------------------------------
def eliminar_piezas():
    print("\n=== ELIMINAR PIEZA ===")
    id_piezasportafolio = input("Introduce el ID de la pieza a eliminar: ")
    confirmacion = input("¿Seguro que deseas eliminarla? (S/N): ").lower()

    if confirmacion == "s":
        sql = "DELETE FROM piezasportafolio WHERE id_categoria=%s"
        cursor.execute(sql, (id_piezasportafolio,))
        conexion.commit()
        print("Pieza eliminada correctamente.")
    else:
        print("Operación cancelada.")

# ---------------------------------------------------------
# MENÚ PRINCIPAL
# ---------------------------------------------------------
while True:
    print("""
--------------------------------------------
Bienvenido al Gestor de Piezas
--------------------------------------------
1. Insertar pieza
2. Listar piezas
3. Actualizar piezas
4. Eliminar pieza
5. Salir
--------------------------------------------
""")

    opcion = input("Elige una opción (1-5): ")

    if opcion == "1":
        insertar_piezas()
    elif opcion == "2":
        listar_piezas()
    elif opcion == "3":
        actualizar_piezas()
    elif opcion == "4":
        eliminar_piezas()
    elif opcion == "5":
        print("Gracias por usar el Gestor de Piezas. ¡Hasta pronto!")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")

# ---------------------------------------------------------
# CIERRE DE CONEXIÓN
# ---------------------------------------------------------
conexion.close()


#Este simulacro integra todos los conceptos fundamentales de Python y MySQL vistos en clase: conexión a bases de datos, estructuras de control, bucles, entrada por teclado y operaciones CRUD. Representa la base de cualquier aplicación de gestión real, combinando la lógica de programación con el manejo de información persistente.
