import sqlite3
from marca import Marca
from modelo import Modelo 
from auto import Auto
conexion=sqlite3.connect("taller.db")
cursor=conexion.cursor()
modelo_yaris = Modelo("Yaris", Marca("Toyota"))
auto = Auto("AB1234", 2018, modelo_yaris) 
print(auto.ingresar())
conexion.close