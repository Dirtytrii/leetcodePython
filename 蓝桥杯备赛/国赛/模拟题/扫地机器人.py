# 输入描述
# N个方格区域，有k台机器人
# 第i台机器人在第ai个位置
# 第一行包含两个整数 N,K
#
# 接下来 K 行，每行一个整数 A
#
# 其中，1≤K<N≤105，1≤Ai≤N
# 输出描述
#
# 输出一个整数表示答案。


def check(robots, clear_area, total_area, num_of_robots):
    """
    该函数用于计算在有num_of_robots的情况下，每个机器人扫clear_area个区域，
    能否扫完total_area的面积，能则返回Ture
    """
    # 当前打扫过的最大位置
    cleared_area = 0
    # 遍历机器人数组
    for j in range(1, num_of_robots + 1):
        # 判断当前机器人向左扫clear个位置，能否把左边都扫完
        if robots[j] - clear_area <= cleared_area:
            # 判断机器人是否需要再扫左侧位置
            if robots[j] <= cleared_area:
                # 机器人直接往右侧扫clear个位置
                cleared_area = robots[j] + clear_area - 1
            else:
                # 当左侧未扫时，在原来的基础上直接扫clear个位置
                cleared_area += clear_area
        else:
            # 当有机器人扫clear个位置无法完成左侧任务时，返回false
            return False

    return cleared_area >= total_area


if __name__ == '__main__':
    # 接受题目参数
    n, k = map(int, input().split())
    a = [0] * (k + 1)
    for i in range(1, k + 1):
        a[i] = int(input())
    # 将机器人位置排序
    a.sort()
    # 左右边界
    l, r = 0, n
    num = -1

    while r >= l:
        m = (l + r) // 2
        # 判断机器人每个扫m面积能否完成
        if check(a, m, n, k):
            r = m - 1
            num = m
        else:
            l = m + 1

    print((num - 1) * 2)
