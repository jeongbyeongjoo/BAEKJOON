# 1시간 3분
# 여기 마지막 로직보고 외워야 함

N, K = map(int, input().split())
M = []
dir = []

for _ in range(N):
    m, d = input().split()
    M.append(int(m))
    dir.append(d)

points = []

if dir[0] == 'R':
    points.append((0, 1))
    points.append((M[0], -1))
else:
    points.append((0, -1))
    points.append((-M[0], 1))

for i in range(1, N):
    if dir[i] == 'R':
        points.append((points[-1][0], 1))
        points.append((points[-1][0] + M[i], -1))
    else:
        points.append((points[-1][0], -1))
        points.append((points[-1][0] - M[i], 1))

points.sort()

x_list = []
cnt = 0

for x, v in points:
    if v == 1:
        cnt += 1
    elif v == -1:
        cnt -= 1
    x_list.append((cnt, x))

sum = 0    

for i in range(1, len(x_list)):
    if x_list[i][0] >= K-1 and x_list[i-1][0] >= K:
        sum += x_list[i][1] - x_list[i-1][1]

print(sum)