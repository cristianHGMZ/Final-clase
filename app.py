import tkinter as tk
from boleta import Boleta
from validador_boleta import ValidadorBoleta
from alerta_boleta import AlertaBoleta

class App:
    def __init__(self, master):
        self.master = master
        master.title("Validar Boleta")

        self.id_label = tk.Label(master, text="ID de Boleta:")
        self.id_label.pack()

        self.id_entry = tk.Entry(master)
        self.id_entry.pack()

        self.qr_label = tk.Label(master, text="Código QR:")
        self.qr_label.pack()

        self.qr_entry = tk.Entry(master)
        self.qr_entry.pack()

        self.barras_label = tk.Label(master, text="Código de Barras:")
        self.barras_label.pack()

        self.barras_entry = tk.Entry(master)
        self.barras_entry.pack()

        self.escanear_button = tk.Button(master, text="Escanear", command=self.escanear_boleta)
        self.escanear_button.pack()

        self.offline_button = tk.Button(master, text="Validar Offline", command=self.validar_offline_boleta)
        self.offline_button.pack()

        self.validador = ValidadorBoleta()
        self.alerta = AlertaBoleta()

    def escanear_boleta(self):
        id = self.id_entry.get()
        qr = self.qr_entry.get()
        barras = self.barras_entry.get()
        boleta = Boleta(id, qr, barras)
        boleta.escanear(self.validador, self.alerta)

    def validar_offline_boleta(self):
        id = self.id_entry.get()
        qr = self.qr_entry.get()
        barras = self.barras_entry.get()
        boleta = Boleta(id, qr, barras)
        boleta.validar_offline(self.validador, self.alerta)

root = tk.Tk()
app = App(root)
root.mainloop()