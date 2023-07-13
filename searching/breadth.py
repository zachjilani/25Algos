# Time
# O(V + E), where V is the number of nodes and E is the number of edges.
# Space
# O(V)

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
visited = []
q = []
def bfs(visited, graph, node):
  q.append(node)
  visited.append(node)

  while q:
    s = q.pop(0)
    print(s)

    for neighbor in graph[s]:
      if neighbor not in visited:
        visited.append(neighbor)
        q.append(neighbor)

bfs(visited, graph, '5')

# output:
# 5
# 3
# 7
# 2
# 4
# 8


