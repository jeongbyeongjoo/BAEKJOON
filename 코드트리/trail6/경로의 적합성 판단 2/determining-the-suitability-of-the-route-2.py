# 18분

n, m, k = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(m)]
path = list(map(int, input().split()))

uf = [i for i in range(n+1)]

def union(x, y):
    uf[find(x)] = find(y)

def find(x):
    if uf[x] == x:
        return x
    root_node = find(uf[x])
    uf[x] = root_node
    return root_node

for x, y in edges:
    union(x, y)

ans = 1

for i in range(1, k):
    if find(path[i-1]) != find(path[i]):
        ans = 0
        break

print(ans)