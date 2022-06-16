def lengthOfLongestSubstring(s: str) -> int:
    l, r, res = 0, 0, 0
    count = [0] * 256
    count_dup = 0

    while r < len(s):
        count[ord(s[r])] += 1  # 将当前字符纳入统计

        if count[ord(s[r])] == 2:  # 标记重复
            count_dup += 1
        r += 1

        while count_dup > 0:  # 消除重复
            count[ord(s[l])] -= 1  # 去除左指针并右移
            l += 1

            if count[ord(s[l])] == 1:  # 判断去重是否成功
                count_dup -= 1

        res = max(r - l, res)

    return res


if __name__ == '__main__':
    lengthOfLongestSubstring("nfpdmpi")
