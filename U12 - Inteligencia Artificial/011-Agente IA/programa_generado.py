import sqlite3

def create_table():
    conn = sqlite3.connect('clientes.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS clientes
                 (id INTEGER PRIMARY KEY, nombre TEXT, correo TEXT)''')
    conn.commit()
    conn.close()

def insert_cliente(nombre, correo):
    conn = sqlite3.connect('clientes.db')
    c = conn.cursor()
    c.execute("INSERT INTO clientes (nombre, correo) VALUES (?, ?)", (nombre, correo))
    conn.commit()
    conn.close()

def list_clientes():
    conn = sqlite3.connect('clientes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM clientes")
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()

def update_cliente(id, nombre, correo):
    conn = sqlite3.connect('clientes.db')
    c = conn.cursor()
    c.execute("UPDATE clientes SET nombre = ?, correo = ? WHERE id = ?", (nombre, correo, id))
    conn.commit()
    conn.close()

def delete_cliente(id):
    conn = sqlite3.connect('clientes.db')
    c = conn.cursor()
    c.execute("DELETE FROM clientes WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def main():
    create_table()
    while True:
        print("\n1. Crear cliente")
        print("2. Listar clientes")
        print("3. Actualizar cliente")
        print("4. Borrar cliente")
        print("5. Salir")
        choice = input("Elige una opción: ")

        if choice == '1':
            nombre = input("Nombre del cliente: ")
            correo = input("Correo del cliente: ")
            insert_cliente(nombre, correo)
        elif choice == '2':
            list_clientes()
        elif choice == '3':
            id = int(input("ID del cliente a actualizar: "))
            nombre = input("Nuevo nombre: ")
            correo = input("Nuevo correo: ")
            update_cliente(id, nombre, correo)
        elif choice == '4':
            id = int(input("ID del cliente a borrar: "))
            delete_cliente(id)
        elif choice == '5':
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
