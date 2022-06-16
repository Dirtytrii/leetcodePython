# 辗转相除法
from math import sqrt


def gcd_normal(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


# 贝祖数的求解,特殊情况
def extend_gcd(a, b):
    # 回溯条件
    if b == 0:
        return 1, 0
    res = extend_gcd(b, a % b)

    # x1 = y2
    # y1 = x2-a//b*y2
    return res[1], res[0] - a // b * res[1]


# 同余方程的求解 形如ax = b(mod p)
# ax = b(mod p)可化为对ax+py = b求贝祖数 而x0 = x1 % b
def congruence_equation(a, b, p):
    # if b % gcd(a, p) != 0:
    #     return 0

    # 特殊情况的求解（即b == gcd（a，p））
    res = extend_gcd(a, p)
    modify = 1

    if b != gcd(a, p):
        modify = b / gcd(a, p)

    return int((res[0] * modify) % p)


# 判断质数
def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x % 6 != 1 and x % 6 != 5:
        return False

    # 从五开始，步长为6
    for i in range(5, int(sqrt(x)) + 1, 6):
        if x % i == 0 or x % (i + 2) == 0:
            return False
    return True


if __name__ == '__main__':
    print(gcd_normal(104, 40))
    print(gcd(104, 40))
    print(extend_gcd(104, 40))
    print(is_prime(101))
    print(congruence_equation(24869975, 76523, 10007))
