class UF:
    count = 0
    parent = []

    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(0, n + 1)]

    # 查找q节点的根节点
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # 链接两个节点
    def union(self, q, p):
        root_q = self.find(q)
        root_p = self.find(p)

        # 已经链接
        if root_p == root_q:
            return
        # 链接两个节点的根节点并维护count
        self.parent[root_p] = root_q
        self.count -= 1


temp = list(map(int, input().split()))
n = temp[0] * temp[1]
uni = UF(n)

run_time = int(input())

for _ in range(run_time):
    temp = list(map(int, input().split()))
    uni.union(temp[0], temp[1])

print(uni.count)
