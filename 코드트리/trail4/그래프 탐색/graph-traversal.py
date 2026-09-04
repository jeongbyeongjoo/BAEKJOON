n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph = [[] for i in range(n+1)]

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*(n+1)

cnt = 0

def dfs(vertex):
    global cnt
    for curr in graph[vertex]:
        if not visited[curr]:
            if curr != 1:
                cnt += 1
            visited[curr] = True
            dfs(curr)

dfs(1)

print(cnt)