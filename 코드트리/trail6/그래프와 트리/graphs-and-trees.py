import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)


def dfs(x):
    visited[x] = True

    vertex_count = 1
    edge_count = len(graph[x])

    for nxt in graph[x]:
        if not visited[nxt]:
            v, e = dfs(nxt)
            vertex_count += v
            edge_count += e

    return vertex_count, edge_count


answer = 0

for i in range(1, n + 1):
    if not visited[i]:
        v, e = dfs(i)

        # 무방향 그래프라 간선이 양쪽에서 2번 세어짐
        e //= 2

        if e == v - 1:
            answer += 1

print(answer)