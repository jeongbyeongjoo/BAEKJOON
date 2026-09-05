from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r -= 1
c -= 1

q = deque()
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
visited = [[False]*n for _ in range(n)]
max_val = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, z):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] >= z:
        return False
    return True

def bfs(z):
    global max_val
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x = x + dx
            new_y = y + dy
            if can_go(new_x, new_y, z):
                visited[new_x][new_y] = True    
                q.append((new_x, new_y))

q.append((r, c))
visited[r][c] = True
prev_val = grid[r][c]
for _ in range(k):
    bfs(prev_val)

    found = False

    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if visited[i][j]:
                if max_val <= grid[i][j] < prev_val:
                    max_val = grid[i][j]
                    r, c = i, j
                    found = True

    if not found:
        break

    visited = [[False]*n for _ in range(n)]
    q.append((r, c))
    visited[r][c] = True
    max_val = 0
    prev_val = grid[r][c]

print(r+1, c+1)
