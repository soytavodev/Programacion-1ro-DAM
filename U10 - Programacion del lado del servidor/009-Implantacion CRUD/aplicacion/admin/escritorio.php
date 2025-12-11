<!doctype html>
<html lang="es">
	<head>
  	<title>El San Patesto - Panel de control</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="css/estilo.css">
  </head>
  <body>
  	<nav>
    	<button>Noticias</button>
      <button>Autores</button>
    </nav>
    <main>
    	<?php include "inc/read/leer.php"; ?>
      <a href="?accion=nuevo" id="nuevo">+</a>
    </main>
  </body>
</html>
