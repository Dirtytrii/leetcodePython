import copy
from typing import List


def dfs(grid: List[List[str]], r, c):
    # 重置这片土地
    grid[r][c] = '0'
    # 开始访问上下的节点
    if r + 1 < len(grid):
        if grid[r + 1][c] == '1':
            dfs(grid, r + 1, c)
    if r - 1 >= 0:
        if grid[r - 1][c] == '1':
            dfs(grid, r - 1, c)
    # 开始访问左右的节点
    if c + 1 < len(grid[0]):
        if grid[r][c + 1] == '1':
            dfs(grid, r, c + 1)
    if c - 1 >= 0:
        if grid[r][c - 1] == '1':
            dfs(grid, r, c - 1)


# 1.遍历这个二维数组
# 2.若遍历过程中发现‘1’，则以这个节点为根启动搜索，在搜索过程中将所有访问过的节点置为‘0’（将已经访问过的岛屿排除，防止影响遍历）
# 3.继续遍历
def numIslands(grid: List[List[str]]) -> int:
    if len(grid) == 0:
        return 0
    island_num = 0
    # 存储行与列
    row_num, column_num = len(grid), len(grid[0])

    # 遍历数组
    for r in range(row_num):
        for c in range(column_num):
            if grid[r][c] == '1':
                island_num += 1
                # 从这个节点开始搜索并重置这片岛屿
                dfs(grid, r, c)

    return island_num


if __name__ == '__main__':
    # 小岛地图
    my_map = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"],
              ["0", "0", "0", "0", "0"]]
    map_1 = copy.deepcopy(my_map)

    print(numIslands(map_1))
    print(my_map)
