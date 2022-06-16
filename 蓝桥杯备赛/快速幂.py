def quickPow(base, power):
    ans = 1

    while power != 0:
        if power % 2 != 0:
            ans *= base
            power -= 1
        else:
            base *= base
            power /= 2

    return ans


print(quickPow(13, 10))
