from typing import List


def lengthOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        max_n = 0
        for j in range(i):
            if nums[j] < nums[i]:
                max_n = max(max_n, dp[j])
        dp[i] = max_n + 1
    return max(dp)
