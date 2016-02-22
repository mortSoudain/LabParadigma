from Puzzle import Puzzle         #Impo
from Santa import Santa
import time
class Main:
  def __init__(self):
    print "Que desea hacer?"
    print "a - Problema de Rutas"
    print "b - Problema de los regalos"
    eleccion = raw_input()
    while eleccion != 'a' and eleccion != 'b':
      eleccion = raw_input("Ingrese una opcion valida: ")
    
    if eleccion == 'b':
      puzzle = Puzzle()
      start = time.time()
      puzzle.Solve()
      end = time.time()
      print "Resuelto en %2.f segundos" % float(end - start), " y en %d" %len(puzzle.PreviousNode), " movimientos." 
    else:
      print "Ingrese el numero de su eleccion"
      print "1 - Visitando la menor cantidad de comunas"
      print "2 - Para la ruta mas corta"
      eleccion = raw_input()
      while eleccion != '1' and eleccion != '2':
        eleccion = raw_input("Ingrese una eleccion valida: ")
      
      s = Santa()
      if eleccion == '1':
        s.CalcularRutaA()
      else:
        s.CalcularRutaB()
      print s.Ruta
  
m = Main()   