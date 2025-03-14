import tkinter as tk
from boleta import Boleta
from validador_boleta import ValidadorBoleta
from alerta_boleta import AlertaBoleta
from usuario import Usuario

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

        self.nombre_usuario_label = tk.Label(master, text="Nombre Usuario:")
        self.nombre_usuario_label.pack()
        self.nombre_usuario_entry = tk.Entry(master)
        self.nombre_usuario_entry.pack()

        self.rol_usuario_label = tk.Label(master, text="Rol Usuario:")
        self.rol_usuario_label.pack()
        self.rol_usuario_entry = tk.Entry(master)
        self.rol_usuario_entry.pack()

        self.escanear_button = tk.Button(master, text="Escanear", command=self.escanear_boleta)
        self.escanear_button.pack()

        self.offline_button = tk.Button(master, text="Validar Offline", command=self.validar_offline_boleta)
        self.offline_button.pack()

        self.info_label = tk.Label(master, text="")
        self.info_label.pack()

        self.validador = ValidadorBoleta()
        self.alerta = AlertaBoleta()

    def escanear_boleta(self):
        id_boleta = self.id_entry.get()
        qr = self.qr_entry.get()
        barras = self.barras_entry.get()
        nombre_usuario = self.nombre_usuario_entry.get()
        rol_usuario = self.rol_usuario_entry.get()

        if nombre_usuario and rol_usuario:
            usuario = Usuario(id_boleta, nombre_usuario, rol_usuario)
        else:
            usuario = None

        boleta = Boleta(id_boleta, qr, barras, usuario)
        if self.validador.verificar_autenticidad(boleta):
            boleta.estado = "válida"
            self.alerta.generar_alerta("Boleta válida")
        else:
            boleta.estado = "inválida"
            self.alerta.generar_alerta("Boleta inválida")

        self.mostrar_info(boleta)

    def validar_offline_boleta(self):
        id_boleta = self.id_entry.get()
        qr = self.qr_entry.get()
        barras = self.barras_entry.get()
        nombre_usuario = self.nombre_usuario_entry.get()
        rol_usuario = self.rol_usuario_entry.get()

        if nombre_usuario and rol_usuario:
            usuario = Usuario(id_boleta, nombre_usuario, rol_usuario)
        else:
            usuario = None

        boleta = Boleta(id_boleta, qr, barras, usuario)

        if self.validador.validar_offline(boleta):
            self.alerta.generar_alerta("Boleta válida offline")
            boleta.estado = "válida Offline"
        else:
            self.alerta.generar_alerta("Boleta inválida offline")
            boleta.estado = "inválida Offline"

        self.mostrar_info(boleta)

    def mostrar_info(self, boleta):
        info_boleta = boleta.get_info()
        info_usuario = boleta.usuario.get_info() if boleta.usuario else "Usuario: Sin información"
        self.info_label.config(text=f"{info_boleta}\n{info_usuario}")