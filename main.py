
from vehiculo import Vehiculo

v=Vehiculo("ABCD12",2018, True)
v.ingresar ()
print("el auto esta creado")
print(f"la tarifa de este auto es: ${v.tarifa_hora()}")
print (f"los datos de este vehiculo son: annio {v.annio} y patente {v.patente}")
print (v)
