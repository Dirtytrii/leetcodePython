def maxPower(s: str) -> int:
    ans, cnt = 1, 1

    # 遍历S
    for i in range(1, len(s)):
        # 和上一个连续
        if s[i] == s[i - 1]:
            # 当前最大连续加一
            cnt += 1
            # 全局最大连续    
            ans = max(ans, cnt)
        else:
            # 当不再连续时重置开始找下一次的连续
            cnt = 1
    return ans


if __name__ == '__main__':
    print(maxPower("ccbccbb"))
