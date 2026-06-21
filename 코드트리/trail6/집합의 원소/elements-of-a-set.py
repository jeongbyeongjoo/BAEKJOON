# 못품(로직은 다 맞는데 마지막에 같은 집합이 맞는지 확인하는 부분에서 틀림)
# 32분

n, m = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(m)]

uf = [i for i in range(n+1)]

def union(x, y):
    uf[find(x)] = find(y)

def find(x):
    if uf[x] == x:
        return x
    root = find(uf[x])
    uf[x] = root
    return root

for act, x, y in query:
    if act == 0:
        union(x, y)
    else:
        if find(x) == find(y):
            print(1)
        else:
            print(0)

