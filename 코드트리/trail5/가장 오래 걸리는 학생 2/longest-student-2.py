# 14분 59

import heapq

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

INT_MAX = float('inf')

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
dist = [INT_MAX]*(n+1)
dist[n] = 0
pq = []

for u, v, w in edges:
    graph[v].append((u, w))

heapq.heappush(pq, (0, n))

while(pq):
    min_dist, u = heapq.heappop(pq)
    if not visited[u]:
        visited[u] = True
        for v, w in graph[u]:
            if min_dist + w < dist[v]:
                dist[v] = min_dist + w
                heapq.heappush(pq, (dist[v], v))

print(max(dist[1:]))