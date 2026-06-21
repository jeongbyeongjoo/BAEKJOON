# 다시
# 이것도 두번쨰 문제랑 비슷해서 하나로 외우기 (리스트로 풀자)
# idx -> u로 바꾸면 일
import heapq

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

INT_MAX = float('inf')

graph = [[] for _ in range(n+1)]

for u, v, w in edges:
    graph[u].append((v,w)) 

pq = []
visited = [False]*(n+1)
dist = [INT_MAX]*(n+1)
dist[1] = 0

heapq.heappush(pq, (0, 1))
while pq:
    min_dist, index = heapq.heappop(pq)

    if not visited[index]:
        visited[index] = True
        for v, w in graph[index]:
            if min_dist + w < dist[v]:
                dist[v] = min_dist + w
                heapq.heappush(pq, (dist[v], v))

for i in range(2, n+1):
    if dist[i] == INT_MAX:
        print(-1)
    else:
        print(dist[i])