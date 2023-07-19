


maxint = 9999999999

class Graph():
  def __init__(self, vertices):
    self.V = vertices
    self.graph = [[0 for column in range(vertices)]
                  for row in range(vertices)]

  def print_res(self, dist):
    print("Vertex \tDistance from Source")
    for node in range(self.V):
      print(node, "\t", dist[node])

  def min_dist(self, dist, shortest_path_set):

    min = maxint

    for u in range(self.V):
      if dist[u] < min and shortest_path_set[u] == False:
        min = dist[u]
        min_index = u
    return min_index

  def dijkstra(self, source):
    dist = [maxint] * self.V
    dist[source] = 0
    shortest_path_set = [False] * self.V

    for cout in range(self.V):
      x = self.min_dist(dist, shortest_path_set)

      shortest_path_set[x] = True

      for y in range(self.V):
        if self.graph[x][y] > 0 and shortest_path_set[y] == False and dist[y] > dist[x] + self.graph[x][y]:
          dist[y] = dist[x] + self.graph[x][y]

    self.print_res(dist)

g = Graph(6)
g.graph = [[0,4,5,0,0,0],
        [4,0,11,9,7,0],
        [5,11,0,0,3,0],
        [0,9,0,0,13,2],
        [0,7,3,13,0,6],
        [0,0,0,2,6,0],
        ];

g.dijkstra(0)
