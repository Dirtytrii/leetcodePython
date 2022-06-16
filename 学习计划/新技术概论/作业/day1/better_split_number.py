from typing import List


def dp(n: int) -> List[List[int]]:
    m = n
    f = [[0] * (n + 1) for _ in range((n + 1))]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 or j == 1:
                f[i][j] = 1
            elif i == j:
                f[i][j] = f[i][j - 1] + 1
            elif i < j:
                f[i][j] = f[i][i]
            else:
                f[i][j] = f[i - j][j] + f[i][j - 1]

    return f


if __name__ == '__main__':
    print((dp(2019)[-1])[-1])
