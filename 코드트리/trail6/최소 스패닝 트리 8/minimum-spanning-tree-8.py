import heapq

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

INT_MAX = float('inf')

pq = []

graph = [[] for _ in range(n+1)]

visited = [False] * (n+1)
dist = [INT_MAX] * (n+1)
dist[n] = 0

heapq.heappush(pq, (0, n))

ans = 0

for u, v, w in edges:
    graph[u].append((v, w))
    graph[v].append((u, w))

while pq:
    min, u = heapq.heappop(pq)

    if not visited[u]:
        visited[u] = True
        ans += min
        for v, w in graph[u]:
            if dist[v] > w:
                dist[v] = w
                heapq.heappush(pq, (dist[v], v))

print(ans)