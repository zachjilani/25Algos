

maxint = 9999999999

class Graph():
  def __init__(self, vertices):
    self.V = vertices
    self.graph = []

  def add_edges(self, u, v, w):
    self.graph.append([u, v, w])

  def print_res(self, dist):
    print("Vertex \tDistance from Source")
    for node in range(self.V):
      print(node, "\t", dist[node])

  def bellman(self, src):
    dist = [maxint] * self.V
    dist[src] = 0
    for _ in range(self.V - 1):
      for u, v, w in self.graph:
        if dist[u] != maxint and dist[u] + w < dist[v]:
          dist[v] = dist[u] + w

    for u, v, w in self.graph:
      if dist[u] != maxint and dist[u] + w < dist[v]:
        dist[v] = dist[u] + w
    self.print_res(dist)

    return
