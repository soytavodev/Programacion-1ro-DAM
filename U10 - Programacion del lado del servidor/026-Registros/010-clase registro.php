<?php
	session_start();
	class Registro {
      public $registro;

      public function __construct() {
          $this->registro = [];

          $this->registro['servidor'] = $_SERVER;
          $this->registro['get'] = $_GET;
          $this->registro['post'] = $_POST;
          $this->registro['sesion'] = $_SESSION;
      }
  }
	

	$json =  json_encode(
		$registro,
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	);
  
  file_put_contents("log/".date('U').".json", $json);
?>
