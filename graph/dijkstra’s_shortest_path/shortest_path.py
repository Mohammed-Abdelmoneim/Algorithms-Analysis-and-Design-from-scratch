class Vertex:

  def __init__(self, name):
    """
        Initialize a vertex object with a name, visited flag,
        total length, source of total length, and an empty array
        for vertex links (edges).
        """
    self.name = name
    self.visited = False
    self.TotalLength = 0
    self.SourceOfTotalLength = None
    self.VertexLinks = []


class Edge:

  def __init__(self, source, target, weight=0):
    """
        Initialize an edge object with a weight, source vertex,
        and target vertex.
        """
    self.weight = weight
    self.source = source
    self.target = target


# Define Graph class
class Graph:
  # Constructor
  def __init__(self, names):
    self.last_index = 0
    self.Vertices = []
    # Create vertices
    for name in names:
      v = Vertex(name)
      self.Vertices.append(v)
      self.last_index += 1

  # Add edges to vertices
  def AddEdges(self, vertexIndex, targets, weights=None):
    self.Vertices[vertexIndex].VertexLinks = []
    for i in range(len(targets)):
      if weights is not None:
        edge = Edge(self.Vertices[vertexIndex], self.Vertices[targets[i]],
                    weights[i])
      else:
        edge = Edge(self.Vertices[vertexIndex], self.Vertices[targets[i]])
      self.Vertices[vertexIndex].VertexLinks.append(edge)

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
        if not dest.target.Visited:
          q.append(dest.target)
          dest.target.Visited = True
          print(current_vertex.name + " - " + dest.target.name)

    self.RestoreVertices()

  # Restore visited flag to false for all vertices
  def RestoreVertices(self):
    for v in self.Vertices:
      v.Visited = False

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
      if not dest.target.Visited:
        print(current_vertex.name + " - " + dest.target.name)
        self.DFSRecursion(dest.target)

  def Dijkstra(self):
    print("Dijkstra From Graph Class;")
    for i in range(1, len(self.Vertices)):
      self.Vertices[i].TotalLength = float('inf')

    for i in range(len(self.Vertices)):
      current_vertex = self.Vertices[i]
      destinations = current_vertex.VertexLinks
      if destinations is None:
        continue

      for j in range(len(destinations)):
        current_edge = destinations[j]
        new_length = current_vertex.TotalLength + current_edge.weight
        if new_length < current_edge.target.TotalLength:
          current_edge.target.TotalLength = new_length
          current_edge.target.SourceOfTotalLength = current_vertex

    path = self.Vertices[-1].name
    v = self.Vertices[-1]
    while v.SourceOfTotalLength is not None:
      path = v.SourceOfTotalLength.name + " - " + path
      v = v.SourceOfTotalLength
    print(self.Vertices[-1].TotalLength)
    print(path)

    self.RestoreVertices()


class Program:

  def Main(self):
    g = Graph(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])

    g.AddEdges(0, [1, 2, 3], [2, 4, 3])

    g.AddEdges(1, [4, 5, 6], [7, 4, 6])
    g.AddEdges(2, [4, 5, 6], [3, 2, 4])
    g.AddEdges(3, [4, 5, 6], [4, 1, 5])

    g.AddEdges(4, [7, 8], [1, 4])
    g.AddEdges(5, [7, 8], [6, 3])
    g.AddEdges(6, [7, 8], [3, 3])

    g.AddEdges(7, [9], [3])
    g.AddEdges(8, [9], [4])

    g.Dijkstra()


p = Program()
p.Main()
