# 15분 30초
import heapq

n, m = map(int, input().split())
k = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

INT_MAX = float('inf')

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
dist = [INT_MAX]*(n+1)
pq = []

for u, v, w in edges:
    graph[u].append((v, w))
    graph[v].append((u, w))

dist[k] = 0
heapq.heappush(pq, (0, k))

while(pq):
    min_dist, u = heapq.heappop(pq)
    if not visited[u]:
        visited[u] = True
        for v, w in graph[u]:
            if min_dist + w < dist[v]:
                dist[v] = min_dist + w
                heapq.heappush(pq, (dist[v], v))

for i in range(1, n+1):
    if dist[i] == INT_MAX:
        print(-1)
    else:
        print(dist[i])