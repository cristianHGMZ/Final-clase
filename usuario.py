class Usuario:
    def __init__(self, id, nombre, rol):
        self._id = id
        self._nombre = nombre
        self._rol = rol

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def rol(self):
        return self._rol

    def get_info(self):
        return f"Usuario: {self.nombre}, Rol: {self.rol}"
     