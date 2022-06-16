from math import sqrt

# def isPrime(m: int) -> bool:
#     m = int(sqrt(m)) + 1
#     for i in range(2, m):
#         if m % i == 0:
#             return False
#
#     return True


if __name__ == '__main__':
    n = 2 ** 20
    ans = 0

    prime = [True] * (n + 1)

    if n >= 2:
        index = 2
        # 将所有偶数置为false
        while index <= n:
            index += 2
            if index <= n:
                prime[index] = False
        ans += 1

    for num in range(3, n + 1, 2):
        if prime[num]:
            index_of_prime = num
            index = num
            # 将当前质数的整数倍都置为False
            while index_of_prime <= n:
                index_of_prime += index
                if index_of_prime <= n:
                    prime[index_of_prime] = False
            ans += 1

    print(ans)
