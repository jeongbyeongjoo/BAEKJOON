# 다시 풀기
# 34분 40초
# 이거 sort 해야하는거 까먹지 말기!!!
# 이게 MST가 맞는지에 대한 로직이 필요함(해설 천재누)
# find()가 호출되어야 uf의 root가 초기화되는거에 유의!!

n, m = map(int, input().split())
type_arr = [' '] + input().split()
edges = [tuple(map(int, input().split())) for _ in range(m)]

uf = [i for i in range(n+1)]
cnt = [1]*(n+1)

def union(x, y):
    X = find(x)
    Y = find(y)
    uf[X] = Y
    if X != Y:
        cnt[Y] += cnt[X]

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

mst = []
ans = 0

edges.sort(key = lambda x:x[2])

for u, v, w in edges:
    if type_arr[u] != type_arr[v]:
        if find(u) != find(v):
            union(u, v)
            mst.append(w)
            ans = max(ans, cnt[find(u)])

if ans == n:
    is_MST = True
else:
    is_MST = False

if is_MST:
    print(sum(mst))
else:
    print(-1)