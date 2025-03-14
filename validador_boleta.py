import random

class ValidadorBoleta:
    def verificar_autenticidad(self, boleta):
        return random.choice([True, False])

    def validar_offline(self, boleta):
        return random.choice([True, False])
        