from vehiculo import Vehiculo
from auto import Auto
from moto import Moto
from camion import Camion

def main():
    # Instanciación y prueba de Vehiculo genérico
    v = Vehiculo("ABCD12", 2018, True)
    v.ingresar()
    print("Vehículo genérico:")
    print(f"Tarifa por hora: ${v.tarifa_hora()}")
    print(f"Datos: Año {v.annio} | Patente {v.patente}")
    print(v)
    print("-" * 50)

    # Instanciación y prueba de Auto
    auto = Auto("CL6789", 2020)
    auto.ingresar()
    print(auto)
    print(f"Tarifa por hora de Auto: ${auto.tarifa_hora()}")
    print("-" * 50)

    # Instanciación y prueba de Moto
    moto = Moto("MT1234", 2022)
    moto.ingresar()
    print(moto)
    print(f"Tarifa por hora de Moto: ${moto.tarifa_hora()}")
    print("-" * 50)

    # Instanciación y prueba de Camion
    camion = Camion("CM5678", 2015)
    camion.ingresar()
    print(camion)
    print(f"Tarifa por hora de Camión: ${camion.tarifa_hora()}")

if __name__ == "__main__":
    main()
