from typing import List


# 关于判断条件以及答案添加，整体思路没问题。

def solveNQueens(self, n: int) -> List[List[str]]:
    if n == 1:
        return [['Q']]

    def isIllegal(row: int, col: int) -> bool:
        # 行与列判断
        if 'Q' in temp[row]:
            return True
        for i in range(0, row):
            if temp[i][col] == 'Q':
                return True
        # 左上
        temp_row, temp_col = row - 1, col - 1
        while temp_col >= 0 and temp_row >= 0:
            if temp[temp_row][temp_col] == 'Q':
                return True
            temp_col -= 1
            temp_row -= 1
        # 右上
        temp_row, temp_col = row - 1, col + 1
        while temp_col < n and temp_row >= 0:
            if temp[temp_row][temp_col] == 'Q':
                return True
            temp_row -= 1
            temp_col += 1

        return False

    def dfs(row: int):
        if row == n:
            # 添加答案
            temp_ans = [''] * n
            i = 0
            for line in temp:
                temp_ans_line = ''
                for char in line:
                    temp_ans_line += char
                temp_ans[i] = temp_ans_line
                i += 1
            ans.append(temp_ans)
            return

        for col in range(0, n):
            if isIllegal(row, col):
                continue
            temp[row][col] = 'Q'
            dfs(row + 1)
            temp[row][col] = '.'

    temp = [['.' for _ in range(0, n)] for _ in range(0, n)]
    ans = []
    dfs(0)
    return ans
