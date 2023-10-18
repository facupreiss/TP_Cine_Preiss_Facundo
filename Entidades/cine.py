class Cine:
  
  def __init__(self,nombre,direccion):
    self._nombre = nombre
    self._direccion = direccion
    self._programacion = None

  def get_nombre(self):
    return self._nombre

  def set_nombre(self,nombre):
    self._nombre = nombre

  def get_direccion(self):
    return self._direccion

  def set_direccion(self,direccion):
    self._direccion = direccion
