def min_island(grid):
    min_size = None

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                if grid[i][j] == 'L':
                    size = explore(grid, i, j, visited, rows, cols)
                    if min_size is None or size < min_size:
                        min_size = size
    
    return min_size

def explore(grid, i, j, visited, rows, cols):
    if i < 0 or i >= rows:
        return 0
    if j < 0 or j >= cols:
        return 0
    if grid[i][j] == 'W':
        return 0
    if visited[i][j]:
        return 0
    
    visited[i][j] = True
    size = 1

    for (dx, dy) in [(-1,0), (1,0), (0,-1), (0,1)]:
        size += explore(grid, i+dx, j+dy, visited, rows, cols)
    
    return size


grid = [
    ['W', 'L', 'L', 'W', 'W'],
    ['W', 'L', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'L', 'L']
]

print(min_island(grid))
