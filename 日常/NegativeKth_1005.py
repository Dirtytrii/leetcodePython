from typing import List


def largestSumAfterKNegations(nums: List[int], k: int) -> int:
    nums.sort()

    # 对最小的各负数进行操作
    for i in range(0, len(nums)):
        if nums[i] >= 0 or k == 0:
            break
        nums[i] = -nums[i]
        k -= 1

    # 若对负数操作完k还是奇数则挑出最小的数进行取反
    if k != 0 and k % 2 != 0:
        nums.sort()
        nums[0] = -nums[0]
    return sum(nums)
