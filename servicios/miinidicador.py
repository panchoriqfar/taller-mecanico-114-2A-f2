import requests

class MiIndicador:
    BASE_URL ="https://mindicador.cl/api/"

    def __init__(self, timeout=5):
        self.__timeout=timeout

    def valor_hoy(self, codigo):
        url= self.BASE_URL + codigo
        respuesta = requests.get(url, timeout=self.__timeout)
        datos = respuesta.json()
        return datos["serie"][0]["valor"]

    def valor_por_fecha(self, codigo, fecha):
        url = f"{self.BASE_URL}{codigo}/{fecha}"
        respuesta = requests.get(url, timeout=self.__timeout)
        datos = respuesta.json()
        if datos.get("serie") and len(datos["serie"]) > 0:
            return datos["serie"][0]["valor"]
        return None