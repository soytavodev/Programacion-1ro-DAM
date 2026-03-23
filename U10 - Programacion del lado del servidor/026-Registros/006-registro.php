<?php
	$registro = [];
  
  $registro['servidor'] = $_SERVER;
  $registro['get'] = $_GET;
  $registro['post'] = $_POST;
  $registro['sesion'] = $_SESSION;
  
  echo json_encode($registro);
?>
