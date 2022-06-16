def add(num1, num2):
    res = ''
    #  用于遍历两个字符串
    i = len(num1) - 1
    j = len(num2) - 1
    # 进位
    carry = 0
    # 从字符串右端开始遍历两个字符串
    while i >= 0 or j >= 0:
        digit_1 = int(num1[i])
        digit_2 = int(num2[j])
        # 将下标左移一位
        i -= 1
        j -= 1
        # 将数相加并且加上上一次的进位
        sum_num = digit_1 + digit_2 + carry
        # 重置进位
        carry = 0
        # 判断下一次的进位
        if sum_num > 1:
            # 进位操作
            sum_num -= 2
            carry += 1
        # 将计算结果加入到res中（往左边加）
        res = str(sum_num) + res
    if carry > 0:
        return '1' + res
    return res


if __name__ == '__main__':
    print(add('11', '11'))
