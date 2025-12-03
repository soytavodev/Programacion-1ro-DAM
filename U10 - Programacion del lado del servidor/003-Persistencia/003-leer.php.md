<?php
  $archivo = fopen("archivo.txt", "r"); // "r" = leer/read
  //parametros 1.-lo que lees 2.-longitud de lo que lees
  $contenido = fread($archivo,filesize(archivo.txt"));
  echo $contenido;
  fclose($archivo);
?>

