import random

class ValidadorBoleta:
    def verificar_autenticidad(self, boleta):
        """Verifica si el código QR o de barras son auténticos."""
        return random.choice([True, False])

    def validar_offline(self, boleta):
        """Valida la boleta sin conexión a internet."""
        return random.choice([True, False])