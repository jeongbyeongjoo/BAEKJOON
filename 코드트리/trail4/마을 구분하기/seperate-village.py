# 27분 30초

import sys

sys.setrecursionlimit(1000000)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

human_cnt = 0

def dfs(x, y):
    global human_cnt

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    visited[x][y] = True
    human_cnt += 1

    for dx, dy in zip(dxs, dys):
        new_x = x + dx
        new_y = y + dy

        if can_go(new_x, new_y):
            dfs(new_x, new_y)

village_cnt = 0
arr = []

for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j] == 1:
            human_cnt = 0
            dfs(i, j)
            village_cnt += 1
            arr.append(human_cnt)
 
print(village_cnt)
arr.sort()

for elem in arr:
    print(elem)