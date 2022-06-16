# 快速幂算法
def myPow(x, n):
    res = 1
    flag = True
    if n < 0:
        n = -n
        flag = False
    while n > 0:
        # 当n为大于1的奇数时，res存放的是求解过程中被取出的单个次方
        # 当n为1时，res乘上x（不断减半次方数中生成的结果数）
        if n % 2 != 0:
            res *= x
        n = n >> 1
        x *= x

    if flag:
        return res
    else:
        return 1 / res


print(myPow(2, 10))
print(myPow(2, -2))
