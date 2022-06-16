def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    s1_count = [0] * 26

    # 统计s1
    for c1 in range(0, 26):
        s1_count[c1] = s1.count(chr(c1 + 97))

    for i in range(0, len(s2)):
        # 初始化子串的统计
        s2_count = [0] * 26

        j = i + len(s1)
        if j > len(s2):
            break

        # 统计i~j
        temp = s2[i:j]

        for c2 in range(0, 26):
            s2_count[c2] = temp.count(chr(c2 + 97))

        if s1_count == s2_count:
            return True

    return False


if __name__ == '__main__':
    print(checkInclusion("ab", "eidbaooo"))
