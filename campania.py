from error import LargoExcedidoError
from anuncio import Video, Display, Social

class Campania:
    def __init__(self, nombre, fecha_inicio, fecha_termino, anuncios_data):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self._anuncios = []
        for formato, datos in anuncios_data:
            anuncio = self._crear_anuncio(formato, datos)
            self._anuncios.append(anuncio)

    @staticmethod
    def _crear_anuncio(formato, datos):
        if formato == "Video":
            return Video(**datos)
        elif formato == "Display":
            return Display(**datos)
        elif formato == "Social":
            return Social(**datos)
        else:
            raise ValueError(f"Formato {formato} no es válido")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if len(value) > 250:
            raise LargoExcedidoError("El nombre de la campaña excede el largo permitido")
        self._nombre = value

    @property
    def anuncios(self):
        return self._anuncios

    def __str__(self):
        count_video = sum(1 for anuncio in self._anuncios if isinstance(anuncio, Video))
        count_display = sum(1 for anuncio in self._anuncios if isinstance(anuncio, Display))
        count_social = sum(1 for anuncio in self._anuncios if isinstance(anuncio, Social))
        return f"Nombre de la campaña: {self.nombre}\nAnuncios: {count_video} Video, {count_display} Display, {count_social} Social"
