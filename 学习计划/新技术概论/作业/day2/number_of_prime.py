def isPrime(num: int):
    if num == 2 or num == 3:
        return True
    # 在6x加减1的范围内
    if num % 6 == 1 or num % 6 == 5:
        for j in range(5, num, 6):
            if num % j == 0 or num % (j + 2) == 0:
                return False
        return True
    else:
        return False


if __name__ == '__main__':
    count = 0
    for i in range(2, 2 ** 10):
        if isPrime(i):
            count += 1

    print(count)
