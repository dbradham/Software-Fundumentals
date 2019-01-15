#  File: Graph.py

# Description: A graph is created from an input data file called graph.txt. There is one edge per line. Each edge is of the
# form - fromVertex, toVertex, and weight. If the weight is not given, a default weight of 1 is assigned to that edge. After the list
# of edges is populated, a label is defined for the starting vertex. This is the starting vertex for both the Depth First Search and
# Breadth First Search. After the starting vertex is identified, both searches are performed and a number of tests are performed.

#  Student Name: David Bradham

#  Student UT EID: dmb3767

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 4/26

#  Date Last Modified: 4/27
class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def wasVisited (self):
    return self.visited

  # determine the label of the vertex
  def getLabel (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)
class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []
    
  # check if a vertex already exists in the graph
  def hasVertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False

  # get index from vertex label
  def getIndex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if ((self.Vertices[i]).label == label):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def addVertex (self, label):
    if not self.hasVertex (label):
      self.Vertices.append (Vertex(label))

      # add a new column in the adjacency matrix for the new Vertex
      nVert = len(self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append (0)
      
      # add a new row for the new Vertex in the adjacency matrix
      newRow = []
      for i in range (nVert):
        newRow.append (0)
      self.adjMat.append (newRow)

  # add weighted directed edge to graph
  def addDirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def addUndirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v
  def getAdjUnvisitedVertex (self, v):
    nVert = len(self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
        return i
    return -1

  # do the depth first search in a graph
  def dfs (self, v):
    # create a Stack
    theStack = Stack()
    visited = []
    # mark vertex v as visited and push on the stack
    (self.Vertices[v]).visited = True
    visited.append(self.Vertices[v].label)
    theStack.push (v)

    # vist other vertices according to depth
    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theStack.peek())
      if (u == -1): 
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        visited.append(self.Vertices[u].label)
        theStack.push(u)
    # the stack is empty let us reset the falgs
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False
    return visited

  # do breadth first search in a graph
  def bfs(self, v):
    theQueue = Queue()
    visited = []
    self.Vertices[v].visited = True
    visited.append(self.Vertices[v].label)
    theQueue.enqueue(v)
    while not theQueue.isEmpty():
      u = self.getAdjUnvisitedVertex(v)
      if u == -1:
        v = theQueue.dequeue()
      else:
        self.Vertices[u].visited = True
        visited.append(self.Vertices[u].label)
        theQueue.enqueue(u)
    return visited
      
  # get edge weight between two vertices
  # return -1 if edge does not exist
  def getEdgeWeight (self, fromVertexLabel, toVertexLabel):
    if self.adjMat[self.getIndex(fromVertexLabel)][self.getIndex(toVertexLabel)] != 0:
      return self.adjMat[self.getIndex(fromVertexLabel)][self.getIndex(toVertexLabel)]
    return -1

  # get a list of immediate neighbors that you can go to from a vertex
  # return empty list if there are none
  def getNeighbors (self, vertexLabel):
    idx = self.getIndex(vertexLabel)
    row = self.adjMat[idx]
    lista = []
    for i in range(len(row) - 1):
      if row[i] != 0:
        lista.append(i)
    return lista

  # get a copy of the list of vertices
  def getVertices (self):
    lista = []
    for i in self.Vertices:
      lista.append(i.label)
    return lista

  # delete an edge from the adjacency matrix
  def deleteEdge (self, fromVertexLabel, toVertexLabel):
    origin = self.getIndex(fromVertexLabel)
    dest = self.getIndex(toVertexLabel)
    self.adjMat[origin][dest] = 0
    self.adjMat[dest][origin] = 0

  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def deleteVertex (self, vertexLabel):
    v = self.getIndex(vertexLabel)
    # delete the vertex from vertex list
    del self.Vertices[v]
    # delete edges to the vertex
    for i in range(len(self.adjMat)):
      self.adjMat[i][v] = 0
    # delete edges from the vertex
    for i in range(len(self.adjMat)):
      self.adjMat[v][i] = 0

def main():
  # create a Graph object
  cities = Graph()

  # open file for reading
  inFile = open ("./graph.txt", "r")

  # read the Vertices
  numVertices = int ((inFile.readline()).strip())
  print (numVertices)

  for i in range (numVertices):
    city = (inFile.readline()).strip()
    print (city)
    cities.addVertex (city)

  # read the edges
  numEdges = int ((inFile.readline()).strip())
  print (numEdges)

  for i in range (numEdges):
    edge = (inFile.readline()).strip()
    print (edge)
    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])

    cities.addDirectedEdge (start, finish, weight)

  # print the adjacency matrix
  print ("\nAdjacency Matrix")
  for i in range (numVertices):
    for j in range (numVertices):
      print (cities.adjMat[i][j], finish == ' ')
    print ()
  print ()

  # read the starting vertex for dfs and bfs
  startVertex = (inFile.readline()).strip()
  print (startVertex)
  # close file
  inFile.close()

  # get the index of the start Vertex
  startIndex = cities.getIndex (startVertex)
  print (startIndex)

  # do depth first search
  print ("\nDepth First Search from " + startVertex)
  print(cities.dfs (startIndex))

  # test breadth first search
  print('Bradth First Search from ' + startVertex, cities.bfs(11))

  print('Test getVertices:', cities.getVertices())

  print('true test:', cities.getEdgeWeight('Houston', 'Atlanta'))
  print('false test', cities.getEdgeWeight('San Francisco', 'Miami'))
  print('neighborhood watch:', cities.getNeighbors('Chicago'))
  print('neighborhood watch:', cities.getNeighbors('Seattle'))

  # test deletion of an edge
  cities.deleteEdge('Houston', 'Atlanta')
  print('Test delete edge:')
  for i in range (numVertices):
    for j in range (numVertices):
      print (cities.adjMat[i][j], finish == ' ')
    print ()
  print ()
  print(cities.getEdgeWeight('Houston', 'Atlanta'))
  # test deletion of a vertex

  cities.deleteVertex('Kansas City')
  print('Test delete vertex')
  for i in cities.Vertices:
    print(i)
  for i in range (numVertices):
    for j in range (numVertices):
      print (cities.adjMat[i][j], finish == ' ')
    print ()
  print ()
main()
