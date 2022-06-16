# 求出一个ax+by=m的解
# 这里的m是gcd（a，b）的整数倍o
def egcd2(a, b, m):
    if m % gcd(a, b) != 0:
        return None
    # before result
    befRes = egcd1(a, b)
    o = m / gcd(a, b)

    return o * befRes[0], o * befRes[1]


# 求出一个ax+by=m的解
# 这里的m就是gcd（a，b）
def egcd1(a, b):
    if b == 0:
        return 1, 0

    res = egcd1(b, a % b)

    return res[1], res[0] - a // b * res[1]


def gcd(a, b) -> int:
    # 当b（上一次的余数）的位置为零时表示上一次调用的ab刚好整除，此时的a（即上一次的b）就是他们的最大公约数
    return a if b == 0 else gcd(b, a % b)


if __name__ == '__main__':
    num = gcd(104, 40)
    print(num)
    print(egcd1(104, 40))
    print(egcd2(104, 40, 16))
