class ValidadorBoleta:
    def verificar_autenticidad(self, boleta):
        if boleta.id:  # Boleta válida si el ID no está vacío
            return True, "Boleta auténtica"
        else:
            return False, "Boleta falsa"

    def validar_offline(self, boleta):
        if boleta.id:  # Boleta válida si el ID no está vacío
            return True, "Boleta validada offline"
        else:
            return False, "Boleta no validada offline"