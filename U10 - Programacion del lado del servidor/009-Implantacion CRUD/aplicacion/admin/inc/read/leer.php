<table>
	<?php
		$host = "localhost";
		$user = "Gustavo";
		$pass = "Hakaishin2.";
		$db   = "periodico";

		$conexion = new mysqli($host, $user, $pass, $db);

    $sql = "SELECT * FROM noticias;";

    $resultado = $conexion->query($sql);
    while ($fila = $resultado->fetch_assoc()) {
			echo "<tr>";
      	echo "<td>".$fila['titulo']."</td>";
        echo "<td>".$fila['fecha_publicacion']."</td>";
        echo "<td>".$fila['autor_id']."</td>";
        echo "<td>".$fila['contenido']."</td>";
         // NUEVO ///////////////
        echo "<td><a href='?accion=editar&id=".$fila['id']."' class='editar' title='Cuidado que vas a editar un dato'>🖊</a></td>";
        echo "<td><a href='?accion=eliminar&id=".$fila['id']."' class='eliminar' title='MAS cuidado todavía porque vas a ELIMINAR un dato'>💩</a></td>";
      	// NUEVO ///////////////
      echo "</tr>";
    }

    $conexion->close();
  ?>
</table>
