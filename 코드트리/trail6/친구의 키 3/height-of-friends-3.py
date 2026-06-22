import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())

    # a가 b보다 키가 크다
    # 즉 a가 먼저 와야 함
    graph[a].append(b)
    indegree[b] += 1

pq = []

# 나보다 앞에 와야 하는 사람이 없는 친구들
for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(pq, i)

answer = []

while pq:
    now = heapq.heappop(pq)
    answer.append(now)

    for nxt in graph[now]:
        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            heapq.heappush(pq, nxt)

# 모든 친구를 세우지 못했다면 사이클이 있다는 뜻
if len(answer) != n:
    print(-1)
else:
    print(*answer)