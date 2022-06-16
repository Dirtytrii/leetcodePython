from typing import List


def dfs(temp: List[int], nums: List[int], ans: List[List[int]]):
    if len(temp) == len(nums):
        ans.append(temp[:])
        return

    for num in nums:
        if num in temp:
            continue
        temp.append(num)
        dfs(temp, nums, ans)
        temp.pop()

    return ans


def permute(nums: List[int]) -> List[List[int]]:
    temp = []
    ans = []
    ans = dfs(temp, nums, ans)
    return ans


if __name__ == '__main__':
    print(permute([1, 2, 3]))
