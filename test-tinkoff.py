class DisJointSets():
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def connected(self, u, v):
        return self.find(u) == self.find(v)

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_x] = root_y
            self.size[root_x] += self.size[root_y]


n, m = input().split()
n = int(n)
m = int(m)

dsu = DisJointSets(n)

for i in range(m):
    query = input().split()
    if query[0] == "1":
        x, y = map(int, query[1:])
        dsu.union(x - 1, y - 1)
    elif query[0] == "2":
        x, y = map(int, query[1:])
        if dsu.find(x - 1) == dsu.find(y - 1):
            print("YES")
        else:
            print("NO")
    elif query[0] == "3":
        x = int(query[1])
        root_x = dsu.find(x - 1)
        print(dsu.size[x - 1])
