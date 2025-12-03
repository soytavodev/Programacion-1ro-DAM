'''
Fecha Magica.py v0.1


Gustavo Delnardo

Un constructor es un tipo especial de función que se llama automáticamente cuando creamos un objeto de una clase. En Python, los constructores se definen con el método __init__. Su trabajo principal es inicializar los atributos del objeto, es decir, darle valores iniciales a las propiedades que tendrá.
'''

import datetime  #importamos el módulo datetime para trabajar con fechas

#creamos un objeto fecha usando el constructor de datetime.date
mi_fecha = datetime.date(2025, 9, 11)  #representa el 11 de septiembre de 2025

#accedemos a las propiedades del objeto fecha
print("Año:", mi_fecha.year)   # Imprime el año
print("Mes:", mi_fecha.month)  # Imprime el mes
print("Día:", mi_fecha.day)    # Imprime el día

#calculamos el día de la semana usando weekday() y isoweekday()
#weekday(): 0 = lunes, 6 = domingo
print("Día de la semana (0=lunes, 6=domingo):", mi_fecha.weekday())

#isoweekday(): 1 = lunes, 7 = domingo
print("Día de la semana (1=lunes, 7=domingo):", mi_fecha.isoweekday())

#al trabajar con el objeto fecha pude ver cómo se usan los constructores para crear un objeto con valores iniciales. También aprendí a acceder a sus propiedades como año, mes y día, y a calcular el día de la semana. Esto me será útil para proyectos donde necesite controlar tiempos o eventos en juegos y otras aplicaciones.

