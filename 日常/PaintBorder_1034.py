from typing import List


def colorBorder(grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    borders = []
    originalColor = grid[row][col]
    visited[row][col] = True
    dfs(grid, row, col, visited, borders, originalColor)

    for x, y in borders:
        grid[x][y] = color
    return grid


def dfs(grid, x, y, visited, borders, originalColor):

    isBorder = False
    m, n = len(grid), len(grid[0])
    direc = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for dx, dy in direc:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < m and 0 <= ny < n and grid[nx][ny] == originalColor):
            isBorder = True
        elif not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(grid, nx, ny, visited, borders, originalColor)
    if isBorder:
        borders.append((x, y))
