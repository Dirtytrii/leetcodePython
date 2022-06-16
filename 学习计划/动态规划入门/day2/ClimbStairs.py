def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2

    step_1, step_2, temp = 1, 2, 0

    # 已知前两个楼梯有多少种方法，则第三个楼梯要么是从前一个楼梯爬上，要么是从前两个楼梯爬上。
    # 所以第三个楼梯的方案数就是前一个的方案数加前两个的方案数
    # 以此类推，第i个楼梯的方案数就是i-2楼梯方案数加i-1楼梯的方案数
    for _ in range(2, n):
        temp = step_1
        step_1 = step_2
        step_2 += temp

    return step_2
