class Boleta:
    def __init__(self, id, codigo_qr, codigo_barras, usuario=None):
        self._id = id
        self._codigo_qr = codigo_qr
        self._codigo_barras = codigo_barras
        self._estado = "pendiente"
        self._usuario = usuario

    @property
    def id(self):
        return self._id

    @property
    def codigo_qr(self):
        return self._codigo_qr

    @property
    def codigo_barras(self):
        return self._codigo_barras

    @property
    def estado(self):
        return self._estado

    @property
    def usuario(self):
        return self._usuario

    @estado.setter
    def estado(self, valor):
        self._estado = valor

    def get_info(self):
        info = f"Boleta ID: {self.id}, Estado: {self.estado}, Dueño: "
        if self.usuario:
            info += self.usuario.nombre
        else:
            info += "Sin dueño asignado"
        return info