from typing import List


def maxProfit(k: int, prices: List[int]) -> int:
    def maxProfitNoLimit(prices: List[int]) -> int:
        dp_i10, dp_i11 = 0, float('-inf')
        dp_i20, dp_i21 = 0, float('-inf')

        for price in prices:
            dp_i20 = max(dp_i20, dp_i21 + price)
            dp_i21 = max(dp_i21, dp_i10 - price)
            dp_i10 = max(dp_i10, dp_i11 + price)
            dp_i11 = max(dp_i11, -price)

        return dp_i20

    n = len(prices)
    if k > n / 2:
        return maxProfitNoLimit(prices)

    dp = [[[0 for _ in range(0, 2)] for _ in range(0, k + 1)] for _ in range(0, n)]

    for i in range(0, n):
        for j in range(k, 0, -1):
            if i == 0:
                dp[i][j][0] = 0
                dp[i][j][1] = float('-inf')
                continue

            dp[i][j][0] = max(
                dp[i - 1][j][0], dp[i - 1][j][1] + prices[i]
            )
            dp[i][j][1] = max(
                dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i]
            )

    return dp[n - 1][k][0]


if __name__ == '__main__':
    print(maxProfit(2, [3, 2, 6, 5, 0, 3]))
