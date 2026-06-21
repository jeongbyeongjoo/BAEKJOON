# 6분 49초
import heapq

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
A, B = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for u, v, w in edges:
    graph[u].append((v, w))
    graph[v].append((u, w))

INT_MAX = float('inf')

pq = []
dist = [INT_MAX]*(n+1)
dist[A] = 0

heapq.heappush(pq, (0, A))

while(pq):
    min_dist, u = heapq.heappop(pq)
    if not visited[u]:
        visited[u] = True
        for v, w in graph[u]:
            if min_dist + w < dist[v]:
                dist[v] = min_dist + w
                heapq.heappush(pq, (dist[v], v))

print(dist[B])