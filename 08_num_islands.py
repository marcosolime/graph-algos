

def num_islands(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                if grid[i][j] == 'L': # dfs only if we hit land
                    explore(grid, i, j, visited, rows, cols)
                    count += 1
    
    return count


def explore(graph, i , j, visited, rows, cols):
    # check bounds
    if i < 0 or i >= rows:
        return
    if j < 0 or j >= cols:
        return
    
    # skip water and visited
    if graph[i][j] == 'W':
        return
    if visited[i][j]:
        return
    
    visited[i][j] = True
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        explore(graph, i+dx, j+dy, visited, rows, cols)


grid = [
    ['W', 'L', 'L', 'W', 'W'],
    ['W', 'L', 'W', 'L', 'L']
]

print(num_islands(grid))