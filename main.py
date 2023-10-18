from Entidades.pelicula import Pelicula
from Entidades.peliculaAnimada import PeliculaAnimada
from Entidades.cine import Cine
from basededatos.conexion import Conexion
import sqlite3 as sql

conexion = Conexion("basededatos/mi_bd.db")
conexion.crearTabla()

a = True
while a:
  
  nro = int(input("Ingrese la opción: \n1-Agregar Pelicula \n2-Modificar Pelicula \n3-Eliminar Pelicula \n4-Listar Peliculas \n5-Agregar Cine \n6-Modificar Cine \n7-Eliminar Cine \n8-Listar Cines \n9-Agregar nueva programacion \n10-Mostrar programacion \n11-Salir \n"))

#AGREGAR PELICULA
  if nro == 1:
    tipo = input("Es una pelicula animada? (si/no)")
    if tipo == "no":
      titulo = input("Ingrese el titulo de la pelicula: ")
      duracion = int(input("Ingrese la duracion de la pelicula: "))
      genero = input("Ingrese el genero de la pelicula: ")
      pelicula = Pelicula(titulo, duracion, genero)
      conexion.agregarPelicula(pelicula)
    elif tipo == "si":
      titulo = input("Ingrese el titulo de la pelicula: ")
      duracion = int(input("Ingrese la duracion de la pelicula: "))
      genero = input("Ingrese el genero de la pelicula: ")
      estudioanimacion = input("Ingrese el estudio de animación: ")
      pelicula = PeliculaAnimada(titulo, duracion, genero, estudioanimacion)
      conexion.agregarPelicula(pelicula)
    else: 
      print("opcion invalida")

#MODIFICAR PELICULA
  elif nro == 2:
    tipo = input("Es una pelicula animada? (si/no)")
    if tipo == "no":
      id = int(input("Ingrese el id de la pelicula a modificar: "))
      titulo = input("Ingrese el titulo de la pelicula: ")
      duracion = int(input("Ingrese la duracion de la pelicula: "))
      genero = input("Ingrese el genero de la pelicula: ")
      pelicula = Pelicula(titulo, duracion, genero)
      conexion.modificarPelicula(id, pelicula)
    elif tipo == "si":
      id = int(input("Ingrese el id de la pelicula a modificar: "))
      titulo = input("Ingrese el titulo de la pelicula: ")
      duracion = int(input("Ingrese la duracion de la pelicula: "))
      genero = input("Ingrese el genero de la pelicula: ")
      estudioAnimacion = input("Ingrese el estudio de animación: ")
      pelicula = PeliculaAnimada(titulo, duracion, genero,estudioAnimacion)
      conexion.modificarPelicula(id, pelicula)
    else:
      print("opcion invalida")

#ELIMINAR PELICULA
  elif nro == 3:
    conexion.eliminarPelicula()

#LISTAR PELICULA
  elif nro == 4:
    conexion.listarPeliculas()

#AGREGAR CINE  
  elif nro == 5:
    conexion.agregarCine()

#MODIFICAR CINE  
  elif nro == 6:
    id = int(input("Ingrese el id del cine a modificar: "))
    nombre = input("Ingrese el nombre del cine: ")
    direccion = input("Ingrese la direccion del cine: ")
    cine = Cine(nombre,direccion)
    conexion.modificarCine(id,cine)

#ELIMINAR CINE  
  elif nro == 7:
    id = int(input("Ingrese el id del cine a eliminar: "))
    conexion.eliminarCine(id)

#LISTAR CINE  
  elif nro == 8:
    cines = conexion.listarCines()
    for cine in cines:
      print(cine)

  elif nro == 9:
    conexion.agregarProgramacion()

  elif nro == 10:
    conexion.mostrarProgramacion()

  elif nro == 11:
    break
  
  else:
    print("Opción inválida")
  
  a = input("Desea continuar? (s/n): ")
  if a == "n":
    a = False
  
conexion.cerrarConexion()