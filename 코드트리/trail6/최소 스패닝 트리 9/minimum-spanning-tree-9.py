import heapq

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

INT_MIN = float('inf')

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
grid = [INT_MIN] * (n+1)
pq = []

for u, v, w in edges:
    graph[u].append((v, w))
    graph[v].append((u, w))

grid[n] = 0
heapq.heappush(pq, (0, n))

ans = 0

while pq:
    min, u = heapq.heappop(pq)

    if not visited[u]:
        visited[u] = True
        ans += min
        for v, w in graph[u]:
            if grid[v] > w:
                grid[v] = w
                heapq.heappush(pq, (w, v))

print(ans)
