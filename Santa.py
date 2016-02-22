# -*- coding: utf-8 -*-
import csv
class Santa:
  def __init__(self):
    f = open('dec.csv','rb')
    reader = csv.reader(f)
    #Distancia entre comunas
    self.DComunas = list(reader)
    self.DComunas.pop(0)
    f = open('dpenalolen.csv', 'rb')
    reader = csv.reader(f)
    #Distancia entre peñalolen y el resto de comunas
    self.DPenalolen = list(reader)
    self.DPenalolen.pop(0)
    f = open('dpuentealto.csv', 'rb')
    reader = csv.reader(f)
    #Distancia entre peñalolen y el resto de comunas
    self.DPuenteAlto = list(reader)
    self.DPuenteAlto.pop(0)
    #Fronteras de la Comuna Candidata
    self.frontera=[]
    self.Inicio = raw_input("Indique la Comuna de Inicio: ")
    self.Inicio = self.Inicio.title()
    self.Destino = raw_input("Indique la Comuna de Destino: ")
    self.Destino = self.Destino.title()
    self.Ruta = []
      
  def CalcularRutaA(self):
    self.Ruta = []
    CActual = self.Inicio
    distancia = float(10000)
    CElegida = 'None'
    
    self.Ruta.append(CActual)
    
    while(CActual != self.Destino):
      self.CalcularFrontera(CActual)

      for f in self.frontera:
        for posible in self.DPuenteAlto:
          if posible[0] == f[0] or posible[0] == f[1]:
            if float(posible[-1]) < float(distancia):
              distancia = float(posible[-1])
              CElegida = posible[0]
              
      self.Ruta.append(CElegida)      
      CActual = CElegida
  
  def CalcularRutaB(self):
    self.Ruta = []
    CActual = self.Inicio
    distancia = float(10000)
    CElegida = 'None'
    
    self.Ruta.append(CActual)
  
    while(CActual != self.Destino):
      self.CalcularFrontera(CActual)

      for f in self.frontera:
        for posible in self.DPenalolen:
          if posible[0] == f[0] or posible[0] == f[1]:
            if float(posible[-1])+float(f[-1]) < float(distancia):
              distancia = float(posible[-1])+float(f[-1])
              CElegida = posible[0]
              
      self.Ruta.append(CElegida)      
      CActual = CElegida
        
    
  def CalcularFrontera(self,CActual):
    self.frontera = []
    for lst in self.DComunas:
      if lst[0] == CActual or lst[1] == CActual:
        self.frontera.append(lst)

