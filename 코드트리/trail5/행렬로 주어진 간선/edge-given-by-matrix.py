# 4분 7초

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dist = graph

for i in range(n):
    dist[i][i] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] and dist[k][j]:
                dist[i][j] = 1

for i in range(n):
    for j in range(n):
        print(dist[i][j], end=" ")
    print()