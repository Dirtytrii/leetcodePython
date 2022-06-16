# 题目描述
#
# 小蓝有黄绿蓝三种颜色的小球，分别为 R,G,BR, G, BR,G,B 个。同样颜色的小球没有区别。
#
# 小蓝将这些小球从左到右排成一排，排完后，将最左边的连续同色小球个数记为 t1t_1t1​，将接下来的连续小球个数记为 t2t_2t2​，
# 以此类推直到最右边的小球。
#
# 请问，总共有多少总摆放小球的方案，使得 t1,t2,⋯t_1, t_2, \cdotst1​,t2​,⋯ 为严格单调递增序列，即 t1≤t2≤t3≤⋯t_1
# \leq t_2 \leq t_3 \leq \cdotst1​≤t2​≤t3​≤⋯。
# 输入描述
#
# 输入一行包含三个整数 R,G,BR, G, BR,G,B。
#
# 其中，0≤R,G,B≤50。0 \leq R, G, B \leq 50。0≤R,G,B≤50。。
# 输出描述
#
# 输出一个整数，表示答案。

# total 当前还剩多少小球 x 指 last颜色的小球使用了多少个
def dfs(total, x, last):
    # 小球刚好用完时，方案数加一
    if total == 0:
        global ans
        ans += 1
        return
    # 遍历三种颜色
    for i in range(3):
        # 若当前颜色和上个颜色相同则跳过
        if i == last:
            continue
        # 上一种颜色的小球有x个，根据递增条件当前颜色有x+1个，但不能超过当前颜色球个数
        for j in range(x + 1, a[i] + 1):
            # 选取j个小球
            a[i] -= j
            if total >= j:
                dfs(total - j, j, i)
            a[i] += j


a = list(map(int, input().split()))
all_ball = sum(a)
ans = 0
dfs(all_ball, 0, -1)
print(ans)
