from typing import List


# 数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。
# 每当你爬上一个阶梯你都要花费对应的体力值，一旦支付了相应的体力值，你就可以选择向上爬一个阶梯或者爬两个阶梯。
# 请你找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。

def minCostClimbingStairs(cost: List[int]) -> int:
    n = len(cost)
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    return dp[n]
    # # 使用贪心每次都选取花费最小的
    # res, now_step, next_step = 0, 0, 0
    #
    # while next_step < len(cost):
    #     if cost[next_step] < cost[next_step + 1]:
    #         now_step = next_step
    #         res += cost[now_step]
    #         next_step += 1
    #     else:
    #         now_step = next_step+1
    #         res += cost[now_step]
    #         next_step += 2
    #
    # return res
