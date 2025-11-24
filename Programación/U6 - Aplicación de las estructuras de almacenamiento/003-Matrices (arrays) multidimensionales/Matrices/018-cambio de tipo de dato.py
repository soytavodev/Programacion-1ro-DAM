tupla = ('manzanas','peras','platanos')
#necesito meter una fruta más
print(tupla)
lista = list(tupla) #convierto una tupla en una lista
print(lista)
lista.append("fresas")

#ahora supongamos que tengo que volver a tupla
nueva_tupla = tuple(lista)
print(nueva_tupla)
