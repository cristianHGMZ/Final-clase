from tkinter import messagebox

class AlertaBoleta:
    @property
    def generar_alerta(self, mensaje):
        return messagebox.showinfo("Alerta", mensaje)
    