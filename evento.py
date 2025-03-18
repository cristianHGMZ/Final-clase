from boleta import Boleta
from validador_boleta import ValidadorBoleta
from usuario import Usuario

class Evento:
    def __init__(self, nombre_Evento, fecha_Evento, ubicacion, capacidad_Evento):
        self._nombre_Evento=nombre_Evento
        self._fecha_Evento=fecha_Evento
        self._ubicacion=ubicacion
        self._capacidad_Evento=capacidad_Evento
        self._validador=ValidadorBoleta()
        self._boleta = []
        self._usuarios=[]
        self._es_oficial=False
        
    def get_Evento(self):
        info=f"Nombre del evento: {self._nombre_Evento}, fecha del evento: {self._fecha_Evento}, Ciudad de la ubicacio: {self._ubicacion} y capacidad de personas: {self._capacidad_Evento}"
        return info
    
    def llevar_info_evento(self):
        self._boleta.get_info(self.get_Evento)
    
    def es_oficial(self, es_oficial):
        if isinstance(es_oficial, bool):
            self._es_oficial = es_oficial
        else:
            raise ValueError("El valor oficial es invalida")
        
    def agregar_boleta(self, boleta):
        
        if isinstance(boleta, Boleta):
            if self._validador.verificar_autenticidad(boleta):
                self._boletas.append(boleta)
            else:
                raise ValueError("La boleta no es auténtica.")
        else:
            raise ValueError("El objeto boleta debe ser una instancia de la clase Boleta.")
        
    def agregar_usuario(self, usuario):
        
        if isinstance(usuario, Usuario):
            self._usuarios.append(usuario)
        else:
            raise ValueError("El objeto usuario debe ser una instancia de la clase Usuario.")
    
    def obtener_boletas(self):
       
        return self._boletas

    def obtener_usuarios(self):
        
        return self._usuarios

       