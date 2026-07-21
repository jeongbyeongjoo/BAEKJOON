# 29분 17초

n = int(input())

arr = []
cnt = [0]*(n+1)

for i in range(n):
    A, B = map(int, input().split())
    arr.append((A, B))

for i in range(n):
    visited = [False]*1001
    for j in range(n):
        if i == j :
            continue
        x1, x2 = arr[j]
        for k in range(x1, x2):
            if not visited[k]:
                visited[k] = True
                cnt[i] += 1

print(max(cnt))