from Entidades.pelicula import Pelicula
from Entidades.cine import Cine
from Entidades.peliculaAnimada import PeliculaAnimada
import sqlite3

class Conexion:
  def __init__(self,nombreBaseDatos):
    self.conexion = sqlite3.connect(nombreBaseDatos)
    self.cursor = self.conexion.cursor()

#CREO LAS TABLAS DE LA BD
  def crearTabla(self):
    self.cursor.execute('''CREATE TABLE IF NOT EXISTS pelicula(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    duracion INTEGER,
    genero TEXT,
    estudioAnimacion TEXT
    )''')

    self.cursor.execute('''CREATE TABLE IF NOT EXISTS cine(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    direccion TEXT
    )''')

    self.cursor.execute('''CREATE TABLE IF NOT EXISTS cine_pelicula(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cine INTEGER,
    id_pelicula INTEGER
    )''')
    
    self.conexion.commit()

#METODOS PARA MANEJAR LAS PELICULAS
  def agregarPelicula(self,pelicula):
    if isinstance(pelicula, Pelicula):
      self.cursor.execute('''INSERT INTO pelicula(titulo,duracion,genero) VALUES (?,?,?)''', (pelicula.get_titulo(),pelicula.get_duracion(),pelicula.get_genero()))
      self.conexion.commit()
    elif isinstance(pelicula, PeliculaAnimada):
      self.cursor.execute('''INSERT INTO pelicula(titulo,duracion,genero,estudioAnimacion) VALUES (?,?,?,?)''', (pelicula.get_titulo(),pelicula.get_duracion(),pelicula.get_genero(),pelicula.get_estudioAnimacion()))
      self.conexion.commit()

  def modificarPelicula(self,id,pelicula):
    if isinstance(pelicula, Pelicula):
      self.cursor.execute('''UPDATE pelicula SET titulo=?, duracion=?, genero=? WHERE id=?''', (pelicula.get_titulo(), pelicula.get_duracion(), pelicula.get_genero(), id))
      self.conexion.commit()
    elif isinstance(pelicula, PeliculaAnimada):
      self.cursor.execute('''UPDATE pelicula SET titulo=?, duracion=?, genero=?,estudioAnimacion=? WHERE id=?''', (pelicula.get_titulo(), pelicula.get_duracion(), pelicula.get_genero(),pelicula.get_estudioAnimacion(), id))
      self.conexion.commit()

  def eliminarPelicula(self):
    id = int(input("Ingrese el id de la pelicula a eliminar: "))
    self.cursor.execute('''DELETE from pelicula where id=?''',(id,))
    self.conexion.commit()
  
  def listarPeliculas(self):
    self.cursor.execute('''SELECT * from pelicula''')
    peliculas = self.cursor.fetchall()
    for pelicula in peliculas:
      if pelicula[4] is None:
        peli = Pelicula(pelicula[1],pelicula[2],pelicula[3])
      elif pelicula[4] is not None:
        peli = PeliculaAnimada(pelicula[1],pelicula[2],pelicula[3],pelicula[4])
      print("ID: ", pelicula[0])
      peli.mostrar_info()
      print("--------------")

  
#METODOS PARA MANEJAR LOS CINES
  def agregarCine(self):
    nombre = input("Ingrese el nombre del cine: ")
    direccion = input("Ingrese la direccion del cine: ")
    cine = Cine(nombre,direccion)
    self.cursor.execute('''INSERT INTO cine(nombre,direccion) VALUES (?,?)''', (cine.get_nombre(),cine.get_direccion()))
    self.conexion.commit()

  def modificarCine(self,id,cine):
    self.cursor.execute('''UPDATE cine SET nombre=?, direccion=? WHERE id=?''', (cine.get_nombre(), cine.get_direccion(), id))
    self.conexion.commit()
  
  def eliminarCine(self,id):
    self.cursor.execute('''DELETE from cine where id=?''',(id,))
    self.conexion.commit()

  def listarCines(self):
    self.cursor.execute('''SELECT * from cine''')
    cine = self.cursor.fetchall()
    return cine

#METODO PARA MANEJAR LA PROGRAMACION
  def agregarProgramacion(self):
    id_cine = int(input("Ingrese ID del cine: "))
    id_pelicula = int(input("Ingrese ID de la pelicula: "))
    self.cursor.execute('''INSERT INTO cine_pelicula(id_cine,id_pelicula) VALUES(?,?)''',(id_cine,id_pelicula))
    self.conexion.commit()

  def mostrarProgramacion(self):
    id_cine = int(input("Ingrese el ID del cine: "))
    self.cursor.execute('''SELECT * FROM cine_pelicula WHERE id_cine=?''', (id_cine,))
    programacion = self.cursor.fetchall()
    for program in programacion:
      self.cursor.execute('''SELECT titulo FROM pelicula WHERE id=?''', (program[2],))
      pelicula = self.cursor.fetchmany(1)
      self.cursor.execute('''SELECT nombre FROM cine WHERE id=?''', (program[1],))
      cine = self.cursor.fetchmany(1)
      print(f'Cine: {cine} Pelicula: {pelicula}') 
      

#METODO PARA CERRAR LA CONEXION A LA BD
  def cerrarConexion(self):
    self.cursor.close()
    self.conexion.close()