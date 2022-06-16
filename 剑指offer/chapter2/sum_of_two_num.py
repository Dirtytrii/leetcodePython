from typing import List


# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
#
# 你可以按任意顺序返回答案。

def twoSum(self, nums: List[int], target: int) -> List[int]:
    # 哈希表法

    hashtable = dict()
    # enumerate --> 将当前对象的数据即下标都取出来分别存放
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        # hash中具体存放的是这个数字的a下标
        hashtable[nums[i]] = i
    return []
# 为什么我是姚宇凡他爹呢 我不明白
