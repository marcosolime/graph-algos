from collections import deque

def shortest_distance(graph, start, end):
    if start == end:
        return 0
    
    queue = deque([(start, 0)]) # (node, distance)
    visited = set([start])

    while queue:
        node, dist = queue.popleft()

        for neighbor in graph.get(node, []):
            if neighbor not in visited: # guard
                if neighbor == end:
                    return dist + 1
                
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    
    return None

graph2 = {
    'A': ['B'],
    'B': ['A'],
    'C': ['D'],
    'D': ['C', 'E'],
    'E': ['D'],
}

print(shortest_distance(graph2, 'A', 'C'))