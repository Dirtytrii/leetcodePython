class UF:
    count = 0
    parent = []

    def __init__(self, n):
        self.count = n
        self.parent = [0] * n

        for i in range(n):
            self.parent[i] = i

    def find(self, x):
        # 查询的同时压缩树
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

        # 查询两个节点根节点是否相同
        return rootQ == rootP

    def count_value(self):
        return self.count

    # 将p和q联通
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootQ == rootP:
            return

        # 将这两个节点的根节点相连
        self.parent[rootQ] = rootP
        self.count -= 1
