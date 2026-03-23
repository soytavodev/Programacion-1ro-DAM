<?php
	session_start();

	$registro = [];

	$registro['servidor'] = $_SERVER;
	$registro['get'] = $_GET;
	$registro['post'] = $_POST;
	$registro['sesion'] = $_SESSION;

	$json =  json_encode(
		$registro,
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	);
  
  file_put_contents("registro.json", $json);
?>
