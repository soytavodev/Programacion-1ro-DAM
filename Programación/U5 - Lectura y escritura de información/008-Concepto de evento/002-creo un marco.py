import tkinter as tk

ventana = tk.Tk()

marco = tk.Frame(ventana)

#DNI NIE
tk.Label(marco,text="Introduce el dni/nie del cliente").pack(padx=20,pady=20)
dninie = tk.Entry(marco)
dninie.pack(padx=10,pady=10)

#NOMBRE
tk.Label(marco,text="Introduce el nombre del cliente").pack(padx=20,pady=20)
nombre = tk.Entry(marco)
nombre.pack(padx=10,pady=10)



marco.pack(padx=20,pady=20)

ventana.mainloop()
