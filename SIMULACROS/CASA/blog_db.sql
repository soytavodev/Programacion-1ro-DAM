-- Creamos la base de datos
CREATE DATABASE blog_db;

-- Seleccionamos la base de datos
USE blog_db;

-- Tabla de usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL
);

-- Tabla de posts
CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    contenido TEXT NOT NULL,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- Tabla de comentarios
CREATE TABLE comentarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    post_id INT NOT NULL,
    usuario_id INT NOT NULL,
    contenido TEXT NOT NULL,
    fecha_comentario DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES posts(id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

INSERT INTO usuarios (nombre, email) VALUES 
('Gustavo Delnardo', 'gustavo@mail.com'),
('Ana Perez', 'ana@mail.com');

INSERT INTO posts (usuario_id, titulo, contenido) VALUES
(1, 'Mi primer post', 'Este es el contenido del primer post'),
(2, 'Hola mundo', 'Contenido del post de Ana');

INSERT INTO comentarios (post_id, usuario_id, contenido) VALUES
(1, 2, '¡Muy buen post!'),
(2, 1, 'Gracias por compartir, Ana');

