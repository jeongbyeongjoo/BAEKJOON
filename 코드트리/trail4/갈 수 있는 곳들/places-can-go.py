# 14분 53초

from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]
visited = [[False]*n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 1:
        return False
    return True

cnt = 0

def bfs():
    global cnt
    while q:
        x, y = q.popleft()

        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

        for dx, dy in zip(dxs, dys):
            new_x = x + dx
            new_y = y + dy
            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                cnt += 1
                q.append((new_x, new_y))

q = deque()

for x, y in points:
    if not visited[x-1][y-1]:
        q.append((x-1, y-1))
        visited[x-1][y-1] = True
        cnt += 1
        bfs()

print(cnt)