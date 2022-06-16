from typing import List


def maxProfit(prices: List[int]) -> int:
    dp = [[0 for _ in range(0, 2)] for _ in range(0, len(prices))]

    for i in range(0, len(prices)):
        if i == 0:
            dp[i][0] = 0
            dp[i][1] = -prices[i]
            continue

        dp[i][0] = max(
            dp[i - 1][0], dp[i - 1][1] + prices[i]
        )
        dp[i][1] = max(
            dp[i - 1][1], -prices[i]
        )

    return dp[-1][0]
