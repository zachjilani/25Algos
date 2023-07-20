

#in place for infinity
maxint = 9999999999

class Graph():
  def __init__(self, vertices):
    self.V = vertices
    self.graph = [[0 for column in range(vertices)]
                  for row in range(vertices)]

  #formatted function to print the result of dijkstras
  def print_res(self, dist):
    print("Vertex \tDistance from Source")
    for node in range(self.V):
      print(node, "\t", dist[node])

  #takes in the distance, and shortest paths
  def min_dist(self, dist, shortest_path_set):
    #sets a minimum to the maxint since we dont know what the dist is yet
    min = maxint

    #for each vertice
    for u in range(self.V):
      #checking if the distance at the index is less than max int and that we havent been there
      if dist[u] < min and shortest_path_set[u] == False:
        #our new min is the number
        min = dist[u]
        #return the index of the vertice
        min_index = u
    return min_index

  def dijkstra(self, source):
    #create a graph of all vertices, with value at maxint
    dist = [maxint] * self.V
    #the first index, which is where you currently are at, will be 0
    dist[source] = 0
    #tracker for the shortest path
    shortest_path_set = [False] * self.V

    for cout in range(self.V):
      #get the index of the closest vertice that hasnt been visited
      x = self.min_dist(dist, shortest_path_set)
      #set index to visited
      shortest_path_set[x] = True

      #for every vertice:
      for y in range(self.V):
        # if the edge from the vertice is greater than 0,
        #has not been visited, and the distance of that edge is greater than the distance of current minimum and the edge length
        if self.graph[x][y] > 0 and shortest_path_set[y] == False and dist[y] > dist[x] + self.graph[x][y]:
          #replace that larger distance with the smaller distance
          dist[y] = dist[x] + self.graph[x][y]

    self.print_res(dist)

#number of vertices
g = Graph(6)
#number of edges for each vertice
g.graph = [[0,4,5,0,0,0], #vertice 0
        [4,0,11,9,7,0], #vertice 1
        [5,11,0,0,3,0], #vertice 2
        [0,9,0,0,13,2], #vertice 3
        [0,7,3,13,0,6], #vertice 4
        [0,0,0,2,6,0],  #vertice 5
        ];
#starting vertice
g.dijkstra(0)
