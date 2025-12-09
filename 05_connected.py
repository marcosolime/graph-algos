

def connected_components_count(graph):
    visited = set()
    count = 0

    for node in graph:
        if explore(graph, node, visited):
            count += 1
    
    return count


def explore(graph, current, visited):
    if current in visited: return False

    visited.add(current)

    for neighbor in graph[current]:
        explore(graph, neighbor, visited) #dfs
    
    return True

graph1 = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C']
}

graph2 = {
    'A': ['B'],
    'B': ['A'],
    'C': ['D'],
    'D': ['C', 'E'],
    'E': ['D'],
}

graph3 = {
    'A': [],
    'B': [],
    'C': [],
}

graph4 = {
    'A': ['B'],
    'B': ['A'],
    'C': [],
    'D': ['E'],
    'E': ['D']
}

graph5 = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['A', 'C']
}
print(connected_components_count(graph5))

