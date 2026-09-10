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

    # Definición del método ingresar para registrar la entrada del vehículo al taller
    def ingresar(self):
        # Se cambia el estado en_taller a True indicando que el vehículo ha ingresado al taller
        self.en_taller = True

    # Definición del método entregar para registrar la salida y entrega del vehículo del taller
    def entregar(self):
        # Se cambia el estado en_taller a False indicando que el vehículo fue entregado
        self.en_taller = False

    # Definición del método tarifa_hora que retorna la tarifa genérica por hora del taller
    def tarifa_hora(self):
        # Se retorna el valor genérico de 5000 como tarifa por hora
        return 5000

    # Definición del método especial __str__ para retornar una representación en texto del vehículo
    def __str__(self):
        estado = "En taller" if self.en_taller else "Fuera del taller"
        return f"Vehículo: {self.patente} | Año: {self.annio} | Estado: {estado}"
