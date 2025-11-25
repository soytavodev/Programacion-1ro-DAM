datos = "uno,dos,tres,cuatro,cinco,seis"

#primero imprimo la cadena
print(datos)
#ahora la parto
partido = datos.split(",")
#ahora imprimo el partido
print(partido)
#ahora quiero unirlo todo de nuevo
nueva_cadena = "|".join(partido) #cualquier simbolo vale para separar los elementos
print(nueva_cadena)
