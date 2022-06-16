from math import sqrt


def prime(x):
    if x % 6 != 1 and x % 6 != 5:
        return False

    for j in range(x, int(sqrt(x)) + 1, 6):
        if x % j == 0 or x % (j + 2) == 0:
            return False
    return True


def pu_prime(x):
    not_prime_nums = ['0', '1', '4', '6', '8', '9']

    s = str(x)

    for not_prime_num in not_prime_nums:
        if not_prime_num in s:
            return False

    return True


if __name__ == '__main__':
    res = 2

    for i in range(4, 20210606):
        if prime(i):
            if pu_prime(i):
                res += 1

    print(res)
