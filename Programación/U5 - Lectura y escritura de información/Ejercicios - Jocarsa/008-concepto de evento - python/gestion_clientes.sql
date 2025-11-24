CREATE USER 'tavo'@'localhost' IDENTIFIED BY 'Hakaishin2.';
GRANT ALL PRIVILEGES ON *.* TO 'tavo'@'localhost';
FLUSH PRIVILEGES;

ALTER USER 'tavo'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Hakaishin2.';
GRANT ALL PRIVILEGES ON *.* TO 'tavo'@'localhost';
FLUSH PRIVILEGES;
EXIT;


CREATE DATABASE clientesdb;
USE clientesdb;

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dni VARCHAR(20),
    nombre VARCHAR(50),
    apellidos VARCHAR(80),
    email VARCHAR(100)
);

