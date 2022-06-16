# O(n) O(n)求斐波那契数的第N项，可优化成常数空间
def fib1(n: int) -> int:
    if n == 0:
        return 0
    if not n > 2:
        return 1
    res_list = [0] * n
    res_list[0], res_list[1] = 1, 1
    for i in range(2, n):
        res_list[i] = res_list[i - 2] + res_list[i - 1]
    return res_list[n - 1]


# 递归解法，效率低
def fib2(n: int) -> int:
    if n == 0:
        return 0
    if not n > 2:
        return 1

    return fib2(n - 2) + fib2(n - 1)


# 常数级空间复杂度
def fib3(n: int) -> int:
    if n == 0:
        return 0
    if n <= 2:
        return 1

    a, b, res = 1, 1, 0

    for i in range(3, n + 1):
        res = a + b
        a = b
        b = res

    return res
