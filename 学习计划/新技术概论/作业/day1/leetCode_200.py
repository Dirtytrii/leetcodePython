from typing import List


class Solution:
    # 深度搜索
    def dfs(self, grid, r, c):
        # 将访问的节点置为零
        grid[r][c] = 0
        nr, nc = len(grid), len(grid[0])
        # 访问（x+-1,y）,(x,y+-1) 这四个节点
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            # 防止 x 或 y 超出边界
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                # 若找到岛屿则继续这个搜索
                self.dfs(grid, x, y)

    # 1.遍历这个二维数组
    # 2.若遍历过程中发现‘1’，则以这个节点为根启动搜索，在搜索过程中将所有访问过的节点置为‘0’（将已经访问过的岛屿排除，防止影响遍历）
    # 3.继续遍历
    def numIslands(self, grid: List[List[str]]) -> int:
        # 存储行列信息用于遍历
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    # 将发现的岛屿排除出遍历
                    self.dfs(grid, r, c)

        return num_islands
