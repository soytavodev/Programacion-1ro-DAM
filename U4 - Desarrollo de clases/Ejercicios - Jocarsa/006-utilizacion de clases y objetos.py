'''
Programa: Redondeos Gamer v0.1

Autor: Gustavo Delnardo

Descripción: Redondeo de números usando métodos dentro de una clase sin funciones externas. En este ejercicio aprenderemos a crear una clase con métodos para redondear números de diferentes formas. Simularemos un juego donde los cálculos matemáticos son parte del desafío para avanzar. Esto nos permitirá practicar cómo definir y usar métodos dentro de clases y aplicar la lógica matemática.
'''

#definición de la clase Matematicas
class Matematicas:
    
    #método para redondear un número al más cercano
    def redondeo(self, numero):
        # Separar la parte entera y decimal
        parte_entera = int(numero)
        parte_decimal = numero - parte_entera
        
        #si la parte decimal es menor a 0.5, redondeamos hacia abajo
        if parte_decimal < 0.5:
            return parte_entera
        else:  # Si es 0.5 o mayor, redondeamos hacia arriba
            return parte_entera + 1
    
    #método para redondear hacia arriba (techo)
    def techo(self, numero):
        parte_entera = int(numero)
        parte_decimal = numero - parte_entera
        
        #siempre subimos un número si hay decimal
        if parte_decimal > 0:
            return parte_entera + 1
        else:
            return parte_entera
    
    #método para redondear hacia abajo (suelo)
    def suelo(self, numero):
        parte_entera = int(numero)
        return parte_entera  # siempre bajamos al entero

# ----------- BLOQUE PRINCIPAL DEL PROGRAMA -----------

#crear una instancia de la clase Matematicas
Mate = Matematicas()

#número a redondear
numero = 4.7

#usar los métodos de la clase y mostrar los resultados
print("Número original:", numero)
print("Redondeo al más cercano:", Mate.redondeo(numero))
print("Redondeo hacia arriba (techo):", Mate.techo(numero))
print("Redondeo hacia abajo (suelo):", Mate.suelo(numero))


#Con este ejercicio aprendimos a crear métodos dentro de una clase para realizar operaciones matemáticas específicas. Vimos cómo aplicar lógica condicional para redondear números hacia arriba, abajo o al más cercano. Estos conceptos se pueden usar en juegos o aplicaciones donde los cálculos numéricos afectan decisiones o resultados de forma práctica.

