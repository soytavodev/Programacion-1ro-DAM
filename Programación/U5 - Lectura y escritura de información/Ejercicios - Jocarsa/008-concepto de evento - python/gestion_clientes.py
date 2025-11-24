'''
Programa: Gestión de Clientes con MySQL v0.1

Gustavo Delnardo

Aplicación con interfaz gráfica (Tkinter) que permite insertar datosde clientes en una base de datos MySQL y mostrarlos en una tabla visual. Incluye eventos, conexión a base de datos y manipulación de widgets.
'''

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# -----------------------------
# CONEXIÓN A LA BASE DE DATOS
# -----------------------------
try:
    conexion = mysql.connector.connect(
        host="localhost",       # servidor local
        user="tavo",            # tu usuario MySQL
        password="Hakaishin2.", # tu contraseña MySQL
        database="clientesdb",  # nombre de la base creada
        ssl_disabled=True       # desactiva SSL para evitar el error 'wrap_socket'
    )
    cursor = conexion.cursor()
except mysql.connector.Error as err:
    print("Error al conectar con la base de datos:", err)
    exit()  #detiene el programa si no hay conexión


# -----------------------------
# FUNCIÓN: Insertar cliente
# -----------------------------
def insertar():
    """
    Evento que se ejecuta al presionar el botón "Insertar cliente".
    Inserta los datos del formulario en la base de datos y actualiza la tabla.
    """
    dni = dninie.get()
    nom = nombre.get()
    ape = apellidos.get()
    mail = email.get()

    if dni == "" or nom == "" or mail == "":
        messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")
        return

    #insertar en la base de datos
    sql = "INSERT INTO clientes (dni, nombre, apellidos, email) VALUES (%s, %s, %s, %s)"
    valores = (dni, nom, ape, mail)
    cursor.execute(sql, valores)
    conexion.commit()

    #limpiar campos
    dninie.delete(0, tk.END)
    nombre.delete(0, tk.END)
    apellidos.delete(0, tk.END)
    email.delete(0, tk.END)

    #actualizar tabla visual
    actualizar_tabla()

    messagebox.showinfo("Éxito", "Cliente insertado correctamente.")


# -----------------------------
# FUNCIÓN: Actualizar tabla
# -----------------------------
def actualizar_tabla():
    """Recarga la tabla con los datos actuales de la base de datos."""
    for fila in arbol.get_children():
        arbol.delete(fila)

    cursor.execute("SELECT dni, nombre, apellidos, email FROM clientes;")
    filas = cursor.fetchall()
    for fila in filas:
        arbol.insert("", "end", values=fila)


# -----------------------------
# INTERFAZ GRÁFICA
# -----------------------------
ventana = tk.Tk()
ventana.title("Gestión de Clientes - Videojuegos y Música")
ventana.geometry("650x500")

marco = tk.Frame(ventana)
marco.pack(padx=20, pady=20)

#campos de entrada
tk.Label(marco, text="Introduce el DNI/NIE del cliente").pack(padx=10, pady=5)
dninie = tk.Entry(marco)
dninie.pack(padx=10, pady=5)

tk.Label(marco, text="Introduce el nombre del cliente").pack(padx=10, pady=5)
nombre = tk.Entry(marco)
nombre.pack(padx=10, pady=5)

tk.Label(marco, text="Introduce los apellidos del cliente").pack(padx=10, pady=5)
apellidos = tk.Entry(marco)
apellidos.pack(padx=10, pady=5)

tk.Label(marco, text="Introduce el email del cliente").pack(padx=10, pady=5)
email = tk.Entry(marco)
email.pack(padx=10, pady=5)

#botón con evento
tk.Button(marco, text="Insertar cliente", command=insertar).pack(padx=10, pady=10)

#tabla de clientes
arbol = ttk.Treeview(ventana, columns=("dni", "nombre", "apellidos", "email"), show="headings")
arbol.heading("dni", text="DNI/NIE")
arbol.heading("nombre", text="Nombre")
arbol.heading("apellidos", text="Apellidos")
arbol.heading("email", text="Email")
arbol.pack(padx=20, pady=20, fill="both", expand=True)

#cargar los datos existentes al iniciar
actualizar_tabla()

#mantener la ventana abierta
ventana.mainloop()

#cerrar la conexión cuando termine
conexion.close()



#Con este ejercicio comprendí cómo funcionan los eventos en Python al hacer que un botón ejecute una acción al pulsarlo. Además, aprendí a conectar la interfaz gráfica con una base de datos MySQL para insertar y mostrar información. Este trabajo me ayuda a entender cómo interactúan Python, SQL y las interfaces gráficas en una aplicación práctica.
