import math

if __name__ == '__main__':
    s = input()
    t = input()
    m, n = len(s), len(t)

    res = math.fabs(m - n)

    # 遍历较短的字符串
    for i in range(m if m < n else n):
        if s[i] != t[i]:
            res += 1

    print(int(res))
