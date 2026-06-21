# 38분 30초

import heapq

n, m, x = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]

for u, v, w in edges:
    graph[u].append((v, w))
    reverse_graph[v].append((u, w))

INT_MAX = float('inf')
INT_MIN = float('-inf')

def solve1(num):
    visited = [False]*(n+1)
    pq = []
    dist = [INT_MAX]*(n+1)
    dist[num] = 0

    heapq.heappush(pq, (0, num))

    while(pq):
        min_dist, u = heapq.heappop(pq)
        if not visited[u]:
            visited[u] = True
            for v, w in graph[u]:
                if min_dist + w < dist[v]:
                    dist[v] = min_dist + w
                    heapq.heappush(pq, (dist[v], v))
    return dist

def solve2(num):
    visited = [False]*(n+1)
    pq = []
    dist = [INT_MAX]*(n+1)
    dist[num] = 0

    heapq.heappush(pq, (0, num))

    while(pq):
        min_dist, u = heapq.heappop(pq)
        if not visited[u]:
            visited[u] = True
            for v, w in reverse_graph[u]:
                if min_dist + w < dist[v]:
                    dist[v] = min_dist + w
                    heapq.heappush(pq, (dist[v], v))
    return dist

dist1 = solve1(x)
dist2 = solve2(x)

max = INT_MIN

for i in range(1, n+1):
    sum = 0
    sum += dist1[i] + dist2[i]
    if sum > max:
        max = sum

print(max)    