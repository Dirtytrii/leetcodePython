class UF:
    parent = []

    # 初始化根集合
    def __init__(self, n):
        self.parent = [0] * (n + 1)
        for i in range(1, n + 1):
            self.parent[i] = i

    # 找到节点的根节点
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # 判断两个节点是否相连
    def connected(self, q, p):
        rootQ = self.find(q)
        rootP = self.find(p)

        return rootQ == rootP

    # 将两个节点相连
    def union(self, q, p):
        rootQ = self.find(q)
        rootP = self.find(p)
        if rootQ == rootP:
            return
            # 将他们的根节点相连
        self.parent[rootQ] = rootP


if __name__ == '__main__':
    n, m = map(int, input().split())
    uf = UF(n)

    op, q, p = [0] * m, [0] * m, [0] * m

    # 接受操作参数
    for i in range(m):
        op[i], q[i], p[i] = map(int, input().split())

    for i in range(m):
        if op[i] == 1:
            uf.union(q[i], p[i])
        else:
            print('YES' if uf.connected(q[i], p[i]) else 'NO')
