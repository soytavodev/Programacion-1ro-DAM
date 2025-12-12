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
      	// Esto se conoce como router (enrutador) /////////////
      	if(isset($_GET['accion'])){
        	if($_GET['accion'] == "nuevo"){
          	include "inc/create/formulario.php";
          }else if($_GET['accion'] == "eliminar"){ 					// Defino la acción eliminar
          	include "inc/delete/eliminar.php";							// En ese caso incluyo eliminar.php
          }else if($_GET['accion'] == "editar"){ 						// Defino la acción editar
          	include "inc/update/formularioactualizar.php";	// En ese caso incluyo el formulario de la edicion.php
          }
        }else{
      		include "inc/read/leer.php"; 
        }
      ?>
      <a href="?accion=nuevo" id="nuevo">+</a>
    </main>
  </body>
</html>
