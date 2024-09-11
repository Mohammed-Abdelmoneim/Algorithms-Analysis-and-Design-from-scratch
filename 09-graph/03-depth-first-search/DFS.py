# Define Vertex class
class Vertex:
  # Constructor
  def __init__(self):
    self.Name = ""
    self.Visited = False
    self.VertexLinks = []


# Define Edge class
class Edge:
  # Constructor
  def __init__(self, source, target, weight=0):
    self.Source = source
    self.Target = target
    self.Weight = weight


# Define Graph class
class Graph:
  # Constructor
  def __init__(self, names):
    self.last_index = 0
    self.Vertices = []
    # Create vertices
    for name in names:
      v = Vertex()
      v.Name = name
      self.Vertices.append(v)
      self.last_index += 1

  # Add edges to vertices
  def AddEdges(self, vertexIndex, targets):
    vertex_links = []
    for target in targets:
      # Create edges
      e = Edge(self.Vertices[vertexIndex], self.Vertices[target])
      vertex_links.append(e)
    self.Vertices[vertexIndex].VertexLinks = vertex_links

  # Perform breadth first search on the graph
  def BFS(self):
    print("BFS From Graph Class;")
    v = len(self.Vertices)
    q = []
    q.append(self.Vertices[0])
    self.Vertices[0].Visited = True

    while q:
      current_vertex = q.pop(0)
      destinations = current_vertex.VertexLinks
      for dest in destinations:
        if not dest.Target.Visited:
          q.append(dest.Target)
          dest.Target.Visited = True
          print(current_vertex.Name + " - " + dest.Target.Name)

    self.RestoreVertices()

# Perform depth first search on the graph
  def DFS(self):
    print("DFS From Graph Class;")
    self.DFSRecursion(self.Vertices[0])
    self.RestoreVertices()
  
  # Recursive function for depth first search
  def DFSRecursion(self, current_vertex):
    current_vertex.Visited = True
    destinations = current_vertex.VertexLinks
    for dest in destinations:
      if not dest.Target.Visited:
        print(current_vertex.Name + " - " + dest.Target.Name)
        self.DFSRecursion(dest.Target)
        
  # Restore visited flag to false for all vertices
  def RestoreVertices(self):
    for v in self.Vertices:
      v.Visited = False


class Program:

  def Main(self):
    g = Graph(["A", "B", "C", "D", "E", "F", "G", "H", "I"])
    g.AddEdges(0, [1, 2])
    g.AddEdges(1, [0, 3, 4])
    g.AddEdges(2, [0, 3, 5])
    g.AddEdges(3, [1, 2, 4])
    g.AddEdges(4, [1, 5])
    g.AddEdges(5, [2, 3, 4, 7])
    g.AddEdges(6, [7, 8])
    g.AddEdges(7, [5, 6, 8])
    g.AddEdges(8, [6, 7])
    g.DFS()


p = Program()
p.Main()
