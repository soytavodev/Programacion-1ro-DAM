<?php
	session_start();
  
  $_SESSION['nombre'] = "Gustavo";
  $_SESSION['apellidos'] = "Delnardo";
  
  foreach($_SESSION as $clave=>$valor){
  	echo $clave.": ".$valor."<br>";
  }
?>
