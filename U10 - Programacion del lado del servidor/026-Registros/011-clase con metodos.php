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

    // Método para convertir a JSON
    public function aJSON() {
        return json_encode(
            $this->registro,
            JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
        );
    }

    // Método para guardar en archivo
    public function guardarArchivo($carpeta = "log") {
        if (!is_dir($carpeta)) {
            mkdir($carpeta, 0777, true);
        }

        $archivo = $carpeta . "/" . date('U') . ".json";
        file_put_contents($archivo, $this->aJSON());

        return $archivo;
    }
}

// Uso
$registro = new Registro();
$registro->guardarArchivo();
?>
