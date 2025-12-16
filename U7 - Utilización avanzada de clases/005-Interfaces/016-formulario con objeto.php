<?php
	
  $cliente = [
  	"nombre" => "Gustavo Enrique",
    "apellidos" => "Delnardo Vallejo",
    "email" => "gustavo1@gmail.com"
  ];
  
  foreach($cliente as $clave=>$valor){
  	echo "<label>".$clave."</label>";
    echo "<input type='text' value='".$valor."'>";
  }
 
?>
