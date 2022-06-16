from math import sqrt


def isPrime(n: int) -> bool:
    for num in range(2, int(sqrt(n)) + 1):
        if n % num == 0:
            return False
    return True


def isPurePrime(n: int) -> bool:
    num_str = str(n)
    if num_str.count('2') + num_str.count('3') + num_str.count('5') + num_str.count('7') == len(num_str):
        return True
    else:
        return False


if __name__ == '__main__':
    ans = 0

    for i in range(1, 20210606):
        if isPrime(i) and isPurePrime(i):
            ans += 1
    print(ans)
