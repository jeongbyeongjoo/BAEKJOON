from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

visited = [[False]*m for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or a[x][y] == 0:
        return False
    return True

def bfs():
    global flag

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x = x + dx
            new_y = y + dy
            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                q.append((new_x, new_y))

q = deque()

visited[0][0] = True
q.append((0, 0))
bfs()

if visited[n-1][m-1]:
    print(1)
else:
    print(0)