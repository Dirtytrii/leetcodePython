def maxPayment(li):
    leng = len(li)
    dp = [[0, 0] for _ in range(leng)]

    '''
    第i个人有两种情况：
    1.接预约： dp[i][1] = dp[i-1][0] + time[i]
    2.不接预约：dp[i][0] = max(dp[i-1][0],dp[i-1][1])
    '''
    # 初始条件：

    print()


if __name__ == '__main__':
    customer_list = [2, 1, 4, 5, 3, 1, 1, 3]

    maxPayment(customer_list)
