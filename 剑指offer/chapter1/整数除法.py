# divisor 除数
# dividend 被除数
def divide(dividend, divisor):
    # flag为偶数则返回值应为正
    flag = 2

    if dividend < 0:
        flag -= 1
        dividend = -dividend
    if divisor < 0:
        flag -= 1
        divisor = -divisor

    res = divideCore(dividend, divisor)

    if flag == 1:
        return -res
    return res


# 该除法自动舍弃余数
def divideCore(dividend, divisor):
    res = 0
    # （解法2） 1.判断被除数是除数的几倍
    # 2.被除数减去n倍的除数，结果值加n
    # 3.继续判断
    while dividend >= divisor:
        # 储存除数
        temp = divisor
        # 存储倍数
        multiply = 1

        # 判断倍数关系
        while dividend > temp:
            temp *= 2
            # 倍数有效，加入到倍数中存储
            if dividend >= temp:
                multiply *= 2

        # 被除数减去N倍的除数
        dividend -= multiply * divisor
        res += multiply

    # # (解法1)每当被除数中取出一个除数，结果值加1
    # while dividend >= divisor:
    #     dividend -= divisor
    #     res += 1
    return res


if __name__ == '__main__':
    print(divide(15468152, 32))
