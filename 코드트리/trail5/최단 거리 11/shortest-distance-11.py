# 27분 16초
# 이거는 역방향으로 구하고 x 출력할때는 정방향으로 해야함 (전 문제랑 순서가 다름)
# if v<min: <- 여기에서 번호가 적은순으로 정점이 선택되는거임 (x 정할 때)

import heapq

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
A, B = map(int, input().split())

INT_MAX = float('inf')

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for u, v, w in edges:
    graph[u].append((v, w))
    graph[v].append((u, w))

pq = []
dist = [INT_MAX]*(n+1)
dist[B] = 0

heapq.heappush(pq, (0, B))

while(pq):
    min_dist, u = heapq.heappop(pq)
    if not visited[u]:
        visited[u] = True
        for v, w in graph[u]:
            if min_dist + w < dist[v]:
                dist[v] = min_dist + w
                heapq.heappush(pq, (dist[v], v))

x = A
list = [x]

while x != B:
    min = INT_MAX
    for v, w in graph[x]:
        if dist[x] == dist[v] + w:
            # 여기서 번호가 가장 작은순을 결정할 수 있게 되는거임
            if v < min:
                min = v
    x = min
    list.append(x)

print(dist[A])

for elem in list:
    print(elem, end=" ")