import tkinter as tk
from boleta import Boleta
from validador_boleta import ValidadorBoleta
from alerta_boleta import AlertaBoleta
from usuario import Usuario
from evento import Evento

class App:
    def __init__(self, master):
        self.master = master
        master.title("Validar Boleta")

        # Campos de entrada para el evento
        self.nombre_evento_label = tk.Label(master, text="Nombre del Evento:")
        self.nombre_evento_label.pack()
        self.nombre_evento_entry = tk.Entry(master)
        self.nombre_evento_entry.pack()

        self.fecha_evento_label = tk.Label(master, text="Fecha del Evento:")
        self.fecha_evento_label.pack()
        self.fecha_evento_entry = tk.Entry(master)
        self.fecha_evento_entry.pack()

        self.ubicacion_evento_label = tk.Label(master, text="Ubicación del Evento:")
        self.ubicacion_evento_label.pack()
        self.ubicacion_evento_entry = tk.Entry(master)
        self.ubicacion_evento_entry.pack()

        self.capacidad_evento_label = tk.Label(master, text="Capacidad del Evento:")
        self.capacidad_evento_label.pack()
        self.capacidad_evento_entry = tk.Entry(master)
        self.capacidad_evento_entry.pack()

        self.crear_evento_button = tk.Button(master, text="Crear Evento", command=self.crear_evento)
        self.crear_evento_button.pack()

        # Campos de entrada para la boleta y el usuario
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

        self.validar_button = tk.Button(master, text="Validar", command=self.validar_boleta) #Se agrega el boton validar
        self.validar_button.pack()

        self.offline_button = tk.Button(master, text="Validar Offline", command=self.validar_offline_boleta)
        self.offline_button.pack()

        self.info_label = tk.Label(master, text="")
        self.info_label.pack()

        self.validador = ValidadorBoleta()
        self.alerta = AlertaBoleta()
        self.evento = None

    def crear_evento(self):
        nombre_evento = self.nombre_evento_entry.get()
        fecha_evento = self.fecha_evento_entry.get()
        ubicacion_evento = self.ubicacion_evento_entry.get()
        capacidad_evento = self.capacidad_evento_entry.get()
        self.evento = Evento(nombre_evento, fecha_evento, ubicacion_evento, capacidad_evento)
        self.info_label.config(text=self.evento.get_Evento())

    def validar_boleta(self): #Se crea el metodo validar_boleta
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
        boleta_valida = self.validador.verificar_autenticidad(boleta) #Se guarda el resultado de la validacion en la variable boleta_valida
        if boleta_valida:
            boleta.estado = "válida"
            self.alerta.generar_alerta("Boleta válida")
        else:
            boleta.estado = "inválida"
            self.alerta.generar_alerta("Boleta inválida")

        if self.evento:
            self.evento.agregar_boleta(boleta)
            if usuario:
                self.evento.agregar_usuario(usuario)

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

        boleta_valida = self.validador.validar_offline(boleta) #Se guarda el resultado de la validacion en la variable boleta_valida

        if boleta_valida:
            self.alerta.generar_alerta("Boleta válida offline")
            boleta.estado = "válida Offline"
        else:
            self.alerta.generar_alerta("Boleta inválida offline")
            boleta.estado = "inválida Offline"

        if self.evento:
            self.evento.agregar_boleta(boleta)
            if usuario:
                self.evento.agregar_usuario(usuario)

        self.mostrar_info(boleta)

    def mostrar_info(self, boleta):
        info_boleta = boleta.get_info()
        info_usuario = boleta.usuario.get_info() if boleta.usuario else "Usuario: Sin información"
        info_evento = self.evento.get_Evento() if self.evento else "Evento: Sin información"
        self.info_label.config(text=f"{info_boleta}\n{info_usuario}\n{info_evento}")