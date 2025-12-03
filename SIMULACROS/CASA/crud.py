"""
Programa: Blog CRUD v0.1
Gustavo Delnardo
CRUD en consola para la base de datos blog_db en MySQL.
"""

import mysql.connector

# ---------------------------------------------------------
# CONEXIÓN A LA BASE DE DATOS
# ---------------------------------------------------------
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_contraseña",
    database="blog_db"
)
cursor = conexion.cursor(dictionary=True)

# ---------------------------------------------------------
# FUNCIONES CRUD
# ---------------------------------------------------------

def listar_posts():
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    for post in posts:
        print(f"{post['id']}: {post['titulo']} (Usuario {post['usuario_id']})")

def crear_post():
    titulo = input("Título del post: ")
    contenido = input("Contenido del post: ")
    usuario_id = input("ID del usuario: ")
    cursor.execute("INSERT INTO posts (usuario_id, titulo, contenido) VALUES (%s, %s, %s)",
                   (usuario_id, titulo, contenido))
    conexion.commit()
    print("Post creado con éxito!")

def actualizar_post():
    post_id = input("ID del post a actualizar: ")
    nuevo_titulo = input("Nuevo título: ")
    nuevo_contenido = input("Nuevo contenido: ")
    cursor.execute("UPDATE posts SET titulo=%s, contenido=%s WHERE id=%s",
                   (nuevo_titulo, nuevo_contenido, post_id))
    conexion.commit()
    print("Post actualizado.")

def eliminar_post():
    post_id = input("ID del post a eliminar: ")
    cursor.execute("DELETE FROM posts WHERE id=%s", (post_id,))
    conexion.commit()
    print("Post eliminado.")

# ---------------------------------------------------------
# MENÚ DE CONSOLA
# ---------------------------------------------------------
while True:
    print("\n--- BLOG CRUD ---")
    print("1. Listar posts")
    print("2. Crear post")
    print("3. Actualizar post")
    print("4. Eliminar post")
    print("5. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        listar_posts()
    elif opcion == "2":
        crear_post()
    elif opcion == "3":
        actualizar_post()
    elif opcion == "4":
        eliminar_post()
    elif opcion == "5":
        break
    else:
        print("Opción inválida")

