import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

# ---------- CONFIGURACIÓN DE CONEXIÓN ----------
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="empresadam",
        password="Empresadam123$",
        database="empresadam"
    )

# ---------- FUNCIÓN PARA INSERTAR CLIENTE ----------
def insertar_cliente():
    dni = dni_entry.get().strip()
    nombre = nombre_entry.get().strip()
    apellidos = apellidos_entry.get().strip()
    email = email_entry.get().strip()

    if not dni or not nombre or not apellidos or not email:
        messagebox.showwarning("Campos vacíos", "Por favor, rellena todos los campos.")
        return

    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO clientes (dni, nombre, apellidos, email)
            VALUES (%s, %s, %s, %s)
        """, (dni, nombre, apellidos, email))
        conn.commit()
        cursor.close()
        conn.close()

        messagebox.showinfo("Éxito", "Cliente insertado correctamente.")
        limpiar_campos()
        cargar_clientes()
    except Error as e:
        messagebox.showerror("Error en la base de datos", str(e))

# ---------- FUNCIÓN PARA CARGAR CLIENTES ----------
def cargar_clientes():
    for item in tree.get_children():
        tree.delete(item)
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT dni, nombre, apellidos, email FROM clientes;")
        for fila in cursor.fetchall():
            tree.insert("", "end", values=fila)
        cursor.close()
        conn.close()
    except Error as e:
        messagebox.showerror("Error al cargar datos", str(e))

# ---------- LIMPIAR CAMPOS ----------
def limpiar_campos():
    dni_entry.delete(0, tk.END)
    nombre_entry.delete(0, tk.END)
    apellidos_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# ---------- ELIMINAR CLIENTE ----------
def eliminar_cliente():
    seleccionado = tree.selection()
    if not seleccionado:
        messagebox.showwarning("Selección requerida", "Selecciona un cliente para eliminar.")
        return

    valores = tree.item(seleccionado, "values")
    dni = valores[0]

    confirm = messagebox.askyesno("Confirmar eliminación", f"¿Eliminar cliente con DNI {dni}?")
    if not confirm:
        return

    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE dni = %s", (dni,))
        conn.commit()
        cursor.close()
        conn.close()

        messagebox.showinfo("Eliminado", f"Cliente {dni} eliminado correctamente.")
        cargar_clientes()
    except Error as e:
        messagebox.showerror("Error al eliminar", str(e))

# ---------- CONFIGURACIÓN DE ESTILO ----------
def configurar_estilo():
    style = ttk.Style()
    style.theme_use("clam")

    # Colores base
    fondo = "#f5f6fa"
    primario = "#4CAF50"
    texto = "#2f3640"

    style.configure("TFrame", background=fondo)
    style.configure("TLabel", background=fondo, foreground=texto, font=("Segoe UI", 10))
    style.configure("TButton", background=primario, foreground="white", font=("Segoe UI", 10, "bold"), padding=6)
    style.map("TButton", background=[("active", "#45a049")])
    style.configure("Treeview", background="white", foreground=texto, fieldbackground="white", font=("Segoe UI", 9))
    style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

# ---------- INTERFAZ GRÁFICA ----------
ventana = tk.Tk()
ventana.title("Gestión de Clientes — Empresadam")
ventana.geometry("750x550")
ventana.resizable(False, False)
ventana.configure(bg="#f5f6fa")

configurar_estilo()

# --- TÍTULO ---
titulo = tk.Label(
    ventana,
    text="📋 GESTIÓN DE CLIENTES",
    font=("Segoe UI", 16, "bold"),
    fg="#2f3640",
    bg="#f5f6fa"
)
titulo.pack(pady=15)

# --- FORMULARIO ---
form_frame = ttk.Frame(ventana)
form_frame.pack(padx=20, pady=10, fill="x")

campos = [
    ("DNI/NIE:", "dni"),
    ("Nombre:", "nombre"),
    ("Apellidos:", "apellidos"),
    ("Email:", "email")
]

# Campos dinámicos
dni_entry = ttk.Entry(form_frame, width=40)
nombre_entry = ttk.Entry(form_frame, width=40)
apellidos_entry = ttk.Entry(form_frame, width=40)
email_entry = ttk.Entry(form_frame, width=40)

for i, (label_text, varname) in enumerate(campos):
    ttk.Label(form_frame, text=label_text).grid(row=i, column=0, padx=5, pady=5, sticky="e")
    globals()[f"{varname}_entry"].grid(row=i, column=1, padx=5, pady=5, sticky="w")

# Botones
boton_frame = ttk.Frame(ventana)
boton_frame.pack(pady=10)

ttk.Button(boton_frame, text="➕ Insertar cliente", command=insertar_cliente).grid(row=0, column=0, padx=10)
ttk.Button(boton_frame, text="🔄 Recargar lista", command=cargar_clientes).grid(row=0, column=1, padx=10)
ttk.Button(boton_frame, text="🗑️ Eliminar cliente", command=eliminar_cliente).grid(row=0, column=2, padx=10)

# --- TABLA ---
tabla_frame = ttk.Frame(ventana)
tabla_frame.pack(padx=20, pady=20, fill="both", expand=True)

tree = ttk.Treeview(
    tabla_frame,
    columns=("dni", "nombre", "apellidos", "email"),
    show="headings",
    height=10
)
tree.heading("dni", text="DNI/NIE")
tree.heading("nombre", text="Nombre")
tree.heading("apellidos", text="Apellidos")
tree.heading("email", text="Email")

tree.column("dni", width=100, anchor="center")
tree.column("nombre", width=150, anchor="center")
tree.column("apellidos", width=150, anchor="center")
tree.column("email", width=200, anchor="center")

# Scrollbar
scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")
tree.pack(fill="both", expand=True)

# --- Cargar clientes al iniciar ---
cargar_clientes()

ventana.mainloop()


