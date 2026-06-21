# 8분 

n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

points = []

for x1, x2 in intervals:
    points.append((x1, 1))
    points.append((x2, -1))

points.sort()

cnt = 0
max_cnt = 0

for x, v in points:
    if v == 1:
        cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
    else:
        cnt -= 1

print(max_cnt)
