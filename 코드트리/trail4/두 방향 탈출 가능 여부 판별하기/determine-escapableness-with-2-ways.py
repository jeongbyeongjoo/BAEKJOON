n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def in_range(x, y):
    if 0 <= x <= n-1 and 0 <= y <= m-1:
        return True
    return False

def can_go(x, y):
    if not in_range(x, y):
        return False
    if grid[x][y] == 0 or visited[x][y]:
        return False
    return True

data = 0

def dfs(x, y):
    global data
    if x == n-1 and y == m-1:
        data = 1

    dxs, dys = [0, 1], [1, 0]

    for dx, dy in zip(dxs, dys):
        new_x = x + dx
        new_y = y + dy

        if can_go(new_x, new_y):
            visited[new_x][new_y] = True
            dfs(new_x, new_y)

visited[0][0] = True
dfs(0, 0)

print(data)
