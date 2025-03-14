from tkinter import messagebox

class AlertaBoleta:
    def generar_alerta(self, mensaje):
        messagebox.showinfo("Alerta", mensaje)