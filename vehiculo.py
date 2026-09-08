# Se define la clase Vehiculo utilizando la convención estándar PascalCase
class Vehiculo:
    # Método constructor que inicializa los atributos del vehículo al instanciar la clase
    def __init__(self, patente: str, annio: int, en_taller: bool = False):
        # Se asigna la patente (tipo texto) al atributo de instancia del objeto
        self.patente: str = patente
        # Se asigna el año de fabricación (tipo entero) al atributo de instancia del objeto
        self.annio: int = annio
        # Se asigna el estado en taller (tipo booleano, por defecto False) al atributo de instancia
        self.en_taller: bool = en_taller
