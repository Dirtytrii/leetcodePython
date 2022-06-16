def dfs(n, m, used, temp):
    global ans

    # 收敛条件
    if len(temp) == m:
        ans += 1
        return

    for i in range(1, n + 1):
        if not used[i - 1]:
            used[i - 1] = True
            temp.append(i)
            dfs(n, m, used, temp)
            used[i - 1] = False
            temp.pop()

    return ans


if __name__ == '__main__':
    used = [False] * 6
    temp = []
    ans = 0
    print(dfs(6, 6, used, temp))
