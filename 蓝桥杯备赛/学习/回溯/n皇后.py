from typing import List


class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:

        def isIllegal(row, col):
            # 行和列判断
            if 'Q' in temp[row]:
                return True
            i = row - 1
            while i >= 0:
                if temp[i][col] == 'Q':
                    return True
                i -= 1

            # 左上
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if temp[i][j] == 'Q':
                    return True
                i, j = i - 1, j - 1
            # 右上
            i, j = row - 1, col + 1
            while i >= 0 and j < len(temp):
                if temp[i][j] == 'Q':
                    return True
                i, j = i - 1, j + 1

            return False

        def dfs(row):
            if row == len(temp):
                # 逐行转换temp格式并加入结果集中
                ans_list = [''] * n
                for i in range(0, len(temp)):
                    ans_word = ''
                    for j in range(0, len(temp)):
                        ans_word += temp[i][j]
                    ans_list[i] = ans_word
                ans.append(ans_list)
                return

            # 在当前行从1~n遍历能够摆放皇后的位置
            for col in range(0, n):
                # 当前位置不能摆放
                if isIllegal(row, col):
                    continue
                # 选择当前位置摆放皇后
                temp[row][col] = 'Q'
                # 进入下一行的判断
                dfs(row + 1)
                # 取消选择
                temp[row][col] = '.'

        if n == 1:
            return [['Q']]
        temp = [['.' for _ in range(0, n)] for _ in range(0, n)]
        ans = []
        dfs(0)
        return ans
