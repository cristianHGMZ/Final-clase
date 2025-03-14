import random

class ValidadorBoleta:
    def verificar_autenticidad(self, boleta):
        resultado = random.choice([True, False])
        if resultado:
            return True, "Boleta autentica"
        else:
            return False, "Boleta falsa"

    def validar_offline(self, boleta):
        resultado = random.choice([True, False])
        if resultado:
            return True, "Boleta validada offline"
        else:
            return False, "Boleta no validada offline"
        