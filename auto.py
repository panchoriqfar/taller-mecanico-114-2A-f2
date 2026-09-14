from vehiculo import Vehiculo

# Se define la clase Auto que hereda de Vehiculo
class Auto(Vehiculo):
    def tarifa_hora(self):
        # Tarifa por hora para automóvil
        return 6000

    def __str__(self):
        estado = "En taller" if self.en_taller else "Fuera del taller"
        return f"Auto [Patente: {self.patente}, Año: {self.annio}, Estado: {estado}]"
