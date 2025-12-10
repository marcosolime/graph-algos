


def largest_component(graph):
    largest = 0
    visited = set()

    for node in graph:
        size = explore(graph, node, visited)
        if size > largest:
            largest = size
    
    return largest


def explore(graph, cur, visited):
    if cur in visited: return 0

    visited.add(cur)
    size = 1

    for neigh in graph[cur]:
        size += explore(graph, neigh, visited)
    
    return size


graph2 = {
    'A': ['B'],
    'B': ['A'],
    'C': ['D'],
    'D': ['C', 'E'],
    'E': ['D'],
}

print(largest_component(graph2))