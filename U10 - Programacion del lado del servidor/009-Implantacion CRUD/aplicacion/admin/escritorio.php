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
    	<?php
      	if(isset($_GET['accion'])){								// Si hay "accion" en la URL
        	if($_GET['accion'] == "nuevo"){					// Si la acción es "nuevo"
          	include "inc/create/formulario.php";	// En ese caso mete el formulario
          }
        }else{																		// En caso contrario
      		include "inc/read/leer.php"; 						// Enseñame la tabla
        }
      ?>
      <a href="?accion=nuevo" id="nuevo">+</a>
    </main>
  </body>
</html>
