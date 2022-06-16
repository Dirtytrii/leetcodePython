from math import sqrt


def quick_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 6 != 1 and num % 6 != 5:
        return False

    for i in range(5, int(sqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False

    return True


print(quick_prime(65423168754978941564333443358331387))
