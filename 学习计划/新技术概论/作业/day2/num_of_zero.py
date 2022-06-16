def numOfZero(n: int):
    ans = 0
    while n > 0:
        n = n // 5
        ans += n
    return ans


if __name__ == '__main__':
    print(numOfZero(500))
