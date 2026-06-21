# 3분 59초
n, m = map(int, input().split())

dist = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(n):
        dist[i][j + 1] = row[j]

queries = [tuple(map(int, input().split())) for _ in range(m)]

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for x, y in queries:
    print(dist[x][y])
