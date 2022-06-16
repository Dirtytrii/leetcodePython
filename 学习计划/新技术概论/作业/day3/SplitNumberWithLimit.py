def dfs(temp: int, target: int, index: int, limit: int, count: int):
    global ans
    # 收敛条件
    if temp >= target:
        # 符合条件时答案数加一
        if temp == target and count == limit:
            ans += 1
        # 回溯
        return

    for i in range(index, target):
        temp += i
        count += 1
        # 调用自身，将当前下标传入，减少不必要的开支
        dfs(temp, target, i, limit, count)
        # 回溯
        temp -= i
        count -= 1

    return ans


if __name__ == '__main__':
    ans = 0
    print(dfs(0, 10, 1, 3, 0))
