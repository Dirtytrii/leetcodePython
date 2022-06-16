def supPower(a, b):
    power = 0
    for num in b:
        power = power * 10 + num
    return myPow(a, power)


def myPow(x, n):
    res = 1

    while n > 0:
        # 当n为大于1的奇数时，res存放的是求解过程中被取出的单个次方
        # 当n为1时，res乘上x（不断减半次方数中生成的结果数）
        if n % 2 != 0:
            res = (res * x) % 1337
        n = n >> 1
        x = (x * x) % 1337

    return res % 1337


print(supPower(2, [3]))
