<form action="?" method="POST">
	<input type="text" name="nombre">
  <input type="text" name="apellidos">
  <input type="submit">
</form>
<?php
	if(isset($_POST['nombre']){
  	foreach($_POST as $clave=>$valor){
      echo $clave.": ".$valor."<br>";
    }
  }
?>	
