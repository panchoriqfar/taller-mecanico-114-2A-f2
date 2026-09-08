# Se define la clase Vehiculo utilizando la palabra reservada 'class' (en Python se recomienda usar PascalCase)
class Vehiculo:
    # Declaración del atributo 'patente' de tipo texto (cadena de caracteres)
    patente: str
    # Declaración del atributo 'annio' de tipo número entero
    annio: int
    # Declaración del atributo 'en_taller' de tipo booleano (verdadero o falso)
    en_taller: bool

# Se define un alias en minúsculas para compatibilidad si se requiere llamar a la clase como 'vehiculo'
vehiculo = Vehiculo
