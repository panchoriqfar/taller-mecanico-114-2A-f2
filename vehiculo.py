# Se define la clase Vehiculo utilizando la convenciÃ³n estÃ¡ndar PascalCase
class Vehiculo:
    # MÃ©todo constructor que inicializa los atributos del vehÃ­culo al instanciar la clase
    def __init__(self, patente: str, annio: int, en_taller: bool = False):
        # Se asigna la patente (tipo texto) al atributo de instancia del objeto
        self.patente: str = patente
        # Se asigna el aÃ±o de fabricaciÃ³n (tipo entero) al atributo de instancia del objeto
        self.annio: int = annio
        # Se asigna el estado en taller (tipo booleano, por defecto False) al atributo de instancia
        self.en_taller: bool = en_taller
        # Se inicializa el atributo protegido _en_taller correspondiente al estado en taller segÃºn el diagrama
        self._en_taller: bool = en_taller

    # DefiniciÃ³n del mÃ©todo ingresar para registrar la entrada del vehÃ­culo al taller
    def ingresar(self):
        # Se cambia el estado _en_taller a True indicando que el vehÃ­culo ha ingresado al taller
        self._en_taller = True
        # Se sincroniza el atributo en_taller a True
        self.en_taller = True

    # DefiniciÃ³n del mÃ©todo entregar para registrar la salida y entrega del vehÃ­culo del taller
    def entregar(self):
        # Se cambia el estado _en_taller a False indicando que el vehÃ­culo fue entregado
        self._en_taller = False
        # Se sincroniza el atributo en_taller a False
        self.en_taller = False

    # DefiniciÃ³n del mÃ©todo tarifa_hora que retorna la tarifa genÃ©rica por hora del taller
    def tarifa_hora(self):
        # Se retorna el valor genÃ©rico de 5000 como tarifa por hora
        return 5000
