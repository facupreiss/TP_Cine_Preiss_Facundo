from Entidades.pelicula import Pelicula


class PeliculaAnimada(Pelicula):
  def __init__(self,titulo, duracion, genero,estudioAnimacion):
    super().__init__(titulo,duracion,genero)
    self._estudioAnimacion = estudioAnimacion
    
  def get_estudioAnimacion(self):
    return self._estudioAnimacion

  def set_estudioAnimacion(self, estudioAnimacion):
    self._estudioAnimacion = estudioAnimacion

  def mostrar_info(self):
    super().mostrar_info()
    print("Estudio de animacion: ", self._estudioAnimacion)
    