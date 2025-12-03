#esta cadena tiene algo que no quiero (\n)
linea_con_salto = "Esto es una prueba \n"
#lo que quiero es QUITAR algo
#quito \n con "nada"
limpiado = linea_con_salto.replace("\n","")

print(limpiado)
