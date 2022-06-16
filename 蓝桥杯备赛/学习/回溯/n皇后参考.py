from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
            约束条件：
                1. 同一行
                2. 同一列
                3. 对角线
            并且 n X n 的矩阵有 n 个皇后。排除1 和 2 的约束，那么也就是每行 放置1个。

            此时需要满足最后 3 的约束：开始穷举
            每个皇后都 可以再 每行 n 个格子内移动。 穷举所有的可能
            找到同时满足 3 个条件的 放法！ 就是这道题的解题。

            1. 因为是二维矩阵，需要 横纵[x, y] 来标记位置，但一行只能出现一个皇后，我们可以使用一个 n 长的数组 queen，
                来表示每个皇后的纵坐标(对应索引就是横坐标)。 假设 n 为 4 ，第一个皇后可以选 4 个位置， 第二个只能选 剩余3个， 2个 1个。。以此类推
            2. 并且要再满足，对角线 不冲突:
                对角线不冲突需要做的是 通过两个集合 diagonal1， diagonal2表示主对角线, 侧对角线。
                根据规律分别是在一条对角线的1. row - col 相等，2. row + col 相等。 来判断当前元素对角线是否已有元素了

            找到符合条件的 "纵坐标列表后"， 再拼接出答案，添加进结果集
        """

        def getNQueens(queen_row: int):
            """
                param:  queen_row 表示二维矩阵的每一行。因为每一行要选择一个位置放置一个皇后
            """
            # 5. 长度满足n， 进行构造结果，加入到结果列表中
            if queen_row == n:
                ans = list()
                for i in range(n):
                    row[queen[i]] = 'Q'
                    ans.append(''.join(row))
                    # 把更改变回来，下次遍历使用
                    row[queen[i]] = '.'
                rst.append(ans)

            for i in range(n):
                # 1. 横，纵， 对角线冲突，剪枝
                if i in col or queen_row - i in diagonal1 or queen_row + i in diagonal2:
                    continue
                # 2. 维护 状态信息
                diagonal1.add(queen_row - i)
                diagonal2.add(queen_row + i)
                col.add(i)
                queen[queen_row] = i
                # 3. 递归执行下一行
                getNQueens(queen_row + 1)
                # 4. 回溯， 去掉状态的更改
                diagonal1.remove(queen_row - i)
                diagonal2.remove(queen_row + i)
                col.remove(i)
                # 可加可不叫，这位置是否有值， 是 col确定的，回溯col即可
                queen[queen_row] = -1

        # 定义所需变量
        # 5. 返回的结果集
        rst = []
        # 1. 斜对角线
        diagonal1 = set()
        diagonal2 = set()
        # 2. 每一列不能重复
        col = set()
        # 3. 表示皇后位置的数组
        queen = [-1] * n
        # 4. 定义一个 n长数组， 全是 ., 用来最后根据皇后位置，输出结果
        row = ["."] * n

        # 6. 调用函数
        getNQueens(0)
        return rst
