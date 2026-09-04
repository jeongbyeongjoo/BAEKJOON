n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*n for _ in range(n)]
arr = []
cnt = 0
order = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def dfs(x, y):
    global order

    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

    for dx, dy in zip(dxs, dys):
        new_x = x + dx
        new_y = y + dy
        if can_go(new_x, new_y):
            order += 1
            visited[new_x][new_y] = 1
            dfs(new_x, new_y)

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            if not visited[i][j]:
                visited[i][j] = 1
                dfs(i, j)
                cnt += 1
                arr.append(order)
                order = 1


print(cnt)
arr.sort()
for elem in arr:
    print(elem)
