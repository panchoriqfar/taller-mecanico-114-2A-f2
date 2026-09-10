
from vehiculo import Vehiculo

auto=Vehiculo("ABCD12",2018, True)
auto.ingresar ()
print("el auto esta creado")
print(f"la tarifa de este auto es: ${auto.tarifa_hora()}")
print (f"los datos de este vehiculo son: annio {auto.annio} y patente {auto.patente}")
print (auto)