n, w = map(int, input().split())

# 数组形状：
#         物品 0 1 2 3
#     容量
#      0
#      1
#      2
#      3
dp = [[0] * 100] * 100

value = [0] * n
weight = [0] * n

for i in range(0, n):
    weight[i], value[i] = map(int, input().split())

for i in range(1, n + 1):
    for j in range(1, w + 1):
        dp[i][j] = dp[i - 1][j]

        if weight[i - 1] <= j:
            dp[i][j] = max(
                dp[i][j], dp[i - 1][j - weight[i - 1]] + value[i - 1]
            )
a
print(dp[n][w])
# volume_and_wroth = [[0] * 2] * 3
#
# for i in range(0, 3):
#     volume_and_wroth[i] = list(map(int, input().split()))
#
# print(volume_and_wroth)
