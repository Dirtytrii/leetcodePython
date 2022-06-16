n, m = map(int, input().split())  # 处理输入
JZ = [[0] * m for _ in range(n)]  # 初始化n行m列的二维数组
i = 0
for k in range(0, -~max(n, m) >> 1):  # 构造螺旋形矩阵
    for j in range(k, m - k):
        i += 1
        JZ[k][j] = i
    for j in range(k + 1, n - k):
        i += 1
        JZ[j][m - k - 1] = i
    for j in range(n - k - 2, k, -1):
        i += 1
        JZ[n - k - 1][j] = i
    for j in range(n - k - 1, k, -1):
        i += 1
        JZ[j][k] = i
print(JZ[19][19])  # 输出矩阵第20行20列的数字
