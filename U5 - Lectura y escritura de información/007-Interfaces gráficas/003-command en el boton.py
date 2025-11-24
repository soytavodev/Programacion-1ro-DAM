#sudo apt-get install python3-tk
import tkinter as tk

ventana = tk.Tk()

tk.Button(text="Pulsame si te atreves",command=accion).pack(padx=10,pady=10)

ventana.mainloop() #no te salgas
