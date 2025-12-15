CREATE DATABASE tiendaonlinedamdaw;
USE tiendaonlinedamdaw;

--aqui pegáis las tablas

CREATE USER 
'Gustavo'@'localhost' 
IDENTIFIED  BY 'Hakaishin2.';

GRANT USAGE ON *.* TO 'tiendaonlinedamdaw'@'localhost';

ALTER USER 'Gustavo'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON tiendaonlinedamdaw.* 
TO 'Gustavo'@'localhost';

FLUSH PRIVILEGES;
