# 7분 32초

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

uf = [i for i in range(n+1)]

def union(x, y):
    X = find(x)
    Y = find(y)
    uf[X] = Y

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

mst = []
edges.sort(key=lambda x:x[2])

for u, v, w in edges:
    if find(u) != find(v):
        union(u, v)
        mst.append(w)

print(sum(mst))