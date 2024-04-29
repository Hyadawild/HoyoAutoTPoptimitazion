def find_shortest_path(graph, start, end):

  visited = set()  
  distances = {node: float('inf') for node in graph}  
  distances[start] = 0  
  previous = {node: None for node in graph}  

  while visited != set(graph.keys()):
    current_node = min((node for node in graph if node not in visited and distances[node] != float('inf')), key=distances.get)
    visited.add(current_node)

    for neighbor, weight in graph[current_node].items():
      new_distance = distances[current_node] + weight
      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance
        previous[neighbor] = current_node

  if distances[end] == float('inf'):
    return None

  path = []
  current_node = end
  while current_node is not None:
    path.append(current_node)
    current_node = previous[current_node]
  path.reverse()
  return path



graph = {
  'Mondstadt': {'Springvale': 2, 'Windwail Highland': 3, 'Stormbearer Point': 5},
  'Springvale': {'Mondstadt': 2, 'Whispering Woods': 4},
  'Windwail Highland': {'Mondstadt': 3, 'Starsnatch Cliff': 4},
  'Stormbearer Point': {'Mondstadt': 5, 'Liyue Harbor': 7},
  'Whispering Woods': {'Springvale': 4},  
  'Starsnatch Cliff': {'Windwail Highland': 4, 'Guili Plains': 6},
  'Liyue Harbor': {'Stormbearer Point': 7, 'Guili Plains': 2},
  'Guili Plains': {'Starsnatch Cliff': 6, 'Liyue Harbor': 2, 'Qingce Village': 4},
  'Qingce Village': {'Guili Plains': 4, 'Mingyun Village': 5},
  'Mingyun Village': {'Qingce Village': 5}
}



shortest_path = find_shortest_path(graph, 'Mondstadt', 'Liyue Harbor')
print(shortest_path)  
