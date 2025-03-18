from tkinter import messagebox

class AlertaBoleta:
    def generar_alerta(self, mensaje):
        return messagebox.showinfo("Alerta", mensaje)
    