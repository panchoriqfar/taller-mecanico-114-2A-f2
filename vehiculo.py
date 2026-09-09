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
        # Se inicializa el atributo protegido _en_taller correspondiente al estado en taller según el diagrama
        self._en_taller: bool = en_taller

    # Definición del método ingresar para registrar la entrada del vehículo al taller
    def ingresar(self):
        # Se cambia el estado _en_taller a True indicando que el vehículo ha ingresado al taller
        self._en_taller = True
        # Se sincroniza el atributo en_taller a True
        self.en_taller = True

    # Definición del método entregar para registrar la salida y entrega del vehículo del taller
    def entregar(self):
        # Se cambia el estado _en_taller a False indicando que el vehículo fue entregado
        self._en_taller = False
        # Se sincroniza el atributo en_taller a False
        self.en_taller = False
