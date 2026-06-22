from collections import deque

n = int(input())

time = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for i in range(1, n + 1):
    arr = list(map(int, input().split()))

    time[i] = arr[0]

    for pre in arr[1:]:
        if pre == -1:
            break

        # pre를 먼저 지어야 i를 지을 수 있음
        graph[pre].append(i)
        indegree[i] += 1

result = [0] * (n + 1)

q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)
        result[i] = time[i]

while q:
    now = q.popleft()

    for nxt in graph[now]:
        # nxt 건물은 now가 끝난 뒤 지을 수 있음
        result[nxt] = max(result[nxt], result[now] + time[nxt])

        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            q.append(nxt)

for i in range(1, n + 1):
    print(result[i])