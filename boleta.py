class Boleta:
    def __init__(self, id, codigo_qr, codigo_barras):
        self._id = id
        self._codigo_qr = codigo_qr
        self._codigo_barras = codigo_barras
        self._estado = "pendiente"
        
    def escanear(self, validador, alerta):
        """Simula el escaneo de la boleta y verifica su autenticidad."""
        if validador.verificar_autenticidad(self):
            self._estado = "válida"
            alerta.generar_alerta("Boleta válida")
            return True
        else:
            self._estado = "inválida"
            alerta.generar_alerta("Boleta inválida")
            return False
        
    def validar_offline(self, validador, alerta):
        """Valida la boleta sin conexión a internet."""
        if validador.validar_offline(self):
            alerta.generar_alerta("Boleta válida offline")
            return True
        else:
            alerta.generar_alerta("Boleta inválida offline")
            return False

    def obtener_id(self):
        return self._id

    def obtener_codigo_qr(self):
        return self._codigo_qr

    def obtener_codigo_barras(self):
        return self._codigo_barras

    def obtener_estado(self):
        return self._estado
Boleta1 = Boleta(1, 123456, 654321)
print(Boleta1.obtener_id())
print(Boleta1.obtener_codigo_qr())
print(Boleta1.obtener_codigo_barras())
print(Boleta1.obtener_estado())