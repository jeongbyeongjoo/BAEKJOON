# 17분 55초

import heapq

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
A, B = map(int, input().split())

INT_MAX = float('inf')
graph = [[] for _ in range(n+1)]

for u, v, w in edges:
    graph[u].append((v, w))
    graph[v].append((u, w))

visited = [False]*(n+1)
dist = [INT_MAX]*(n+1)
path = [0]*(n+1)
dist[A] = 0
pq = []

heapq.heappush(pq, (0, A))

while(pq):
    min_dist, u = heapq.heappop(pq)
    if not visited[u]:
        visited[u] = True
        for v, w in graph[u]:
            if min_dist + w < dist[v]:
                dist[v] = min_dist + w
                path[v] = u
                heapq.heappush(pq, (dist[v], v))

print(dist[B])

x = B 
list = [B]
while x != A:
    x = path[x]
    list.append(x)

for elem in list[::-1]:
    print(elem, end=" ")