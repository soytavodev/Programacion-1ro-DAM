import mysql.connector

# Conexión a MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_contraseña",
    database="blog_db"
)
cursor = conexion.cursor(dictionary=True)

# Consultamos posts
cursor.execute("""
    SELECT posts.titulo, posts.contenido, usuarios.nombre 
    FROM posts 
    JOIN usuarios ON posts.usuario_id = usuarios.id
""")
posts = cursor.fetchall()

# Generamos HTML dinámico
html_inicio = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi Blog</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <header>
        <h1>Mi Blog Personal</h1>
    </header>
    <main>
"""

html_fin = """
    </main>
</body>
</html>
"""

# Creamos contenido de posts
contenido_posts = ""
for post in posts:
    contenido_posts += f"""
    <article class="post">
        <h2>{post['titulo']}</h2>
        <p>{post['contenido']}</p>
        <small>Por {post['nombre']}</small>
    </article>
    """

# Escribimos el archivo HTML
with open("index.html", "w", encoding="utf-8") as archivo:
    archivo.write(html_inicio + contenido_posts + html_fin)

print("Archivo index.html generado correctamente.")

