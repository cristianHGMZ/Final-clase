from alerta_boleta import AlertaBoleta
class generar_Reporte:
    def __init__(self, ingreso, fecha, numeroAsistentes):
        self._ingreso = ingreso
        self._fecha = fecha
        self._numeroAsistentes = numeroAsistentes
        self._alerta = AlertaBoleta
    
    @property
    def get_Reporte(self):
        reporte = f"Ingreso de la persona: {self._ingreso}, hora y fecha de ingreso: {self._fecha} y cuantos asistentes ingresaron: {self._numeroAsistentes}"
        return reporte
    
    def mostrar_reporte(self):
        self._alerta.generar_alerta(self.get_Reporte)
        
reporte=generar_Reporte("Cristian Gomez", "14/03/2025 a las 10:30", 1)
reporte.mostrar_reporte()