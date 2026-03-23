<?php
	session_start();

	$registro = [];

	$registro['servidor'] = $_SERVER;
	$registro['get'] = $_GET;
	$registro['post'] = $_POST;
	$registro['sesion'] = $_SESSION;

	echo json_encode(
		$registro,
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	);
?>
