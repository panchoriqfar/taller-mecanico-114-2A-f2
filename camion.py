from vehiculo import Vehiculo

# Se define la clase Camion que hereda de Vehiculo
class Camion(Vehiculo):
    def tarifa_hora(self):
        # Tarifa por hora para camión
        return 10000

    def __str__(self):
        estado = "En taller" if self.en_taller else "Fuera del taller"
        return f"Camión [Patente: {self.patente}, Año: {self.annio}, Estado: {estado}]"
