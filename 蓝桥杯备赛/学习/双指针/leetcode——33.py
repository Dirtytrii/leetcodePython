from typing import List


def search(nums: List[int], target: int) -> int:
    nums.sort()
    left = 0
    n = len(nums)
    right = n - 1

    while left <= right:
        mid = int((left + right) / 2)

        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid

    return -1


if __name__ == '__main__':
    print(search([4, 5, 6, 7, 0, 1, 2], 0))
