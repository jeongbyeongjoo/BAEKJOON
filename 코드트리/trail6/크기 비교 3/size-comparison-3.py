import heapq

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
pq = []
list = []

for u, v in edges:
    graph[u].append(v)
    indegree[v] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(pq, i)

while pq:
    u = heapq.heappop(pq)

    list.append(u)

    for v in graph[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            heapq.heappush(pq, v)

for elem in list:
    print(elem, end=" ")
