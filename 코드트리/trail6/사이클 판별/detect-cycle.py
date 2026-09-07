from collections import deque

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

q = deque()
cnt = 0

for u, v in edges:
    graph[u].append(v)
    indegree[v] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    u = q.popleft()
    cnt += 1

    for v in graph[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)

if cnt != n:
    print("Exists")
else:
    print("Not Exists")
