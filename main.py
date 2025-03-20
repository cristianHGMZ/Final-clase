import tkinter as tk
from database import obtener_conexion
from app import App

root = tk.Tk()
app = App(root)
root.mainloop()

conexion = obtener_conexion()
if conexion:
    conexion.close()