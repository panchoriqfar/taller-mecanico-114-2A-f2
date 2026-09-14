from vehiculo import Vehiculo

# Se define la clase Moto que hereda de Vehiculo
class Moto(Vehiculo):
    def tarifa_hora(self):
        # Tarifa por hora para motocicleta
        return 4000

    def __str__(self):
        estado = "En taller" if self.en_taller else "Fuera del taller"
        return f"Moto [Patente: {self.patente}, Año: {self.annio}, Estado: {estado}]"
