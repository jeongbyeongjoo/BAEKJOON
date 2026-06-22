import sys

input = sys.stdin.readline

n, m = map(int, input().split())

INF = 10**15

dist = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 거리는 0
for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())

    # 같은 방향 간선이 여러 개 있을 수도 있으니 최소값 저장
    dist[a][b] = min(dist[a][b], c)

# 플로이드 워셜
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

answer = INF

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            continue

        if dist[i][j] != INF and dist[j][i] != INF:
            answer = min(answer, dist[i][j] + dist[j][i])

if answer == INF:
    print(-1)
else:
    print(answer)