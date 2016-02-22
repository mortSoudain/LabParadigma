import math
class Puzzle:
  def __init__(self):
    self.fronts=[]
    self.GoalNode=['1','2','3','4','5','6','7','8','0']
    #Costo por nivel del objetivo es 0, por conveniencia -1
    self.GoalNode.append(0)
    self.StartNode=['1','4','0','6','2','3','8','7','5']
    #Agrego el Nivel
    self.StartNode.append(1)
    self.PreviousNode=[]
    
  def printPuzzle(self, array):
    s = map(int, array)
    s2 = '\n'.join([str(s[:3]), str(s[3:6]), str(s[6:9])]).replace('0', 'S').replace(',', ' |')
    print s2
        
  def Solve(self):

    nxNode = self.StartNode
    print "Inicio:\n"
    self.printPuzzle(nxNode)
    print
    print "Resolviendo ...\n"
    
    while nxNode[0:9]!=self.GoalNode[0:9]:
      self.sucessor(nxNode)
      nxNode = self.getNextNode()
      #self.printPuzzle(nxNode)
      #print
        
    print 'Resultado:\n'
    self.printPuzzle(nxNode)
        
  #Detecta la fila donde se encuentra el espacio vacio
  def boundries(self,location):
    lst=[[1,2,3],[4,5,6],[7,8,9]]
    low=0
    high=0
    for i in lst:
      if location in i:
        low=i[0]
        high=i[2]
    
    return [low,high]
    
  #Devuelve el siguiente nodo de menor costo heuristico  
  def getNextNode(self):
    nxNode=[]
    tNode=[]
    while True:
      hrCost=100000
      for i in self.fronts:
        if(i[-1]<hrCost):
          hrCost=i[-1]
          nxNode=i[0:-1]
          tNode=i
          
      for Pnode in self.PreviousNode:
        if tNode[0:9] == Pnode[0:9] and tNode in self.fronts:
          self.fronts.remove(tNode)
          break
                  
      else:
        self.PreviousNode.append(tNode)
        self.fronts=[]
        return nxNode

  #Calcula el costo heuristico  
  def heruistic(self,node):
    hDist=0
    
    for i in node[0:9]:
      if i != '0':
        hDist +=math.fabs(node.index(i)-self.GoalNode.index(i))
        
    gLevel = int(node[9])+1
    node[9] = gLevel
    
    totalHerst=hDist+gLevel
           
    node.append(totalHerst)
    return node
        
        
  #Calcula los sucesores del nodo actual y su heuristica  
  def sucessor(self,node=[]):
    subNode=[]
    getZeroLocation=node.index('0')+1
    subNode.extend(node)
    boundry=self.boundries(getZeroLocation)
    
    #Mover Abajo        
    if getZeroLocation+3<=9:
      temp=subNode[node.index('0')]
      subNode[node.index('0')]=subNode[node.index('0')+3]
      subNode[node.index('0')+3]=temp
      self.fronts.append(self.heruistic(subNode))
      subNode=[]
      subNode.extend(node)
      
    #Mover Arriba
    if getZeroLocation-3>=1:
      temp=subNode[node.index('0')]
      subNode[node.index('0')]=subNode[node.index('0')-3]
      subNode[node.index('0')-3]=temp
      self.fronts.append(self.heruistic(subNode))
      subNode=[]
      subNode.extend(node)
    #Mover Izquierda
    if getZeroLocation-1>=boundry[0]:
      temp=subNode[node.index('0')]
      subNode[node.index('0')]=subNode[node.index('0')-1]
      subNode[node.index('0')-1]=temp
      self.fronts.append(self.heruistic(subNode))
      subNode=[]
      subNode.extend(node)
    #Mover Derecha
    if getZeroLocation+1<=boundry[1]:
      temp=subNode[node.index('0')]
      subNode[node.index('0')]=subNode[node.index('0')+1]
      subNode[node.index('0')+1]=temp
      self.fronts.append(self.heruistic(subNode))       