from typing import List


def generate(self, numRows: int) -> List[List[int]]:
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1, 1]]

    dp = [[[] for _ in range(numRows)] for _ in range(numRows)]

    # 初始化数组
    for i in range(0, numRows):
        dp[i][0] = 1
        dp[i][i] = 1

    # j表示行数，k表示行中第几个元素
    # 边界值已定义，行中填充不应超过边界
    for j in range(2, numRows):
        for k in range(1, j):
            dp[j][k] = dp[j - 1][k - 1] + dp[j - 1][k]

    return [dp[-1]]


if __name__ == '__main__':
    print(generate(None, 5))
