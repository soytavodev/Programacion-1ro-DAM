'''
Programa: Suma de Números v0.1

Gustavo Delnardo

En este ejercicio crearemos una interfaz gráfica sencilla usando Tkinter. Permitirá a los jugadores de un juego ingresar dos números y obtener su suma. Aprenderemos cómo usar ventanas, cuadros de entrada, botones y etiquetas en Python.
'''


import tkinter as tk  #importamos la biblioteca Tkinter para la GUI

#función que realiza la suma y muestra el resultado
def calcular():
    #obtenemos los valores de los cuadros de entrada y los convertimos a números
    num1 = float(operando1.get())
    num2 = float(operando2.get())
    suma = num1 + num2
    #mostramos el resultado en la etiqueta
    resultado.config(text=f"Resultado: {suma}")

#crear ventana principal
ventana = tk.Tk()
ventana.title("Suma de Números")
ventana.geometry("300x200")  # Tamaño de la ventana

#campo de entrada para el primer número
operando1 = tk.Entry(ventana)
operando1.pack(padx=10, pady=10)

#campo de entrada para el segundo número
operando2 = tk.Entry(ventana)
operando2.pack(padx=10, pady=10)

#botón para realizar el cálculo
boton = tk.Button(ventana, text="Calcular!", command=calcular)
boton.pack(padx=10, pady=10)

#etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="Aquí va el resultado")
resultado.pack(padx=10, pady=10)

#mostrar la ventana principal
ventana.mainloop()


#Aprendimos a crear una GUI básica en Python con cuadros de entrada, botones y etiquetas. El ejercicio demuestra cómo capturar datos del usuario y mostrar resultados dinámicamente. Estas habilidades son fundamentales para desarrollar aplicaciones de videojuegos y software interactivo.
