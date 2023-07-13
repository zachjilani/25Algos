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


visited = set()

def dfs(visited, graph, node):  #function for dfs
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


dfs(visited, graph, '5')

# output:
# 5
# 3
# 2
# 4
# 8
# 7








