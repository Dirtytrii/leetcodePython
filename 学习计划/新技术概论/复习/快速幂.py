import math


def quick_power(base, power):
    res = 1
    flag = True

    if power < 0:
        power = -power
        flag = False

    while power != 0:
        if power % 2 != 0:
            res *= base
        base *= base
        power = power >> 1

    if flag:
        return res
    else:
        return 1 / res


print(quick_power(2, 100))

print(math.pow(2, 100))
