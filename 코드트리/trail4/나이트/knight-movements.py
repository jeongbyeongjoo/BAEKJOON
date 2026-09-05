from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

q = deque()
dxs, dys = [1, 2, 2, 1, -1, -2, -2, -1], [-2, -1, 1, 2, 2, 1, -1, -2]
visited = [[False]*n for _ in range(n)]
step = [[0]*n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    return True

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x = x + dx
            new_y = y + dy
            if can_go(new_x, new_y):
                visited[new_x][new_y] = True    
                step[new_x][new_y] = step[x][y] + 1
                q.append((new_x, new_y))

q.append((r1, c1))
visited[r1][c1] = True
bfs()


if visited[r2][c2] == 0:
    print(-1)
else:
    print(step[r2][c2])
