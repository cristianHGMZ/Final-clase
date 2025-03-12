from tkinter import messagebox

class AlertaBoleta:
    def generar_alerta(self, mensaje):
        """Genera una alerta con el mensaje especificado."""
        messagebox.showinfo("Alerta", mensaje)