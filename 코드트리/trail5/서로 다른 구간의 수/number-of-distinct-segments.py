# 6분 58초

n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

points = []

for i, (x1, x2) in enumerate(intervals):
    points.append((x1, 1, i))
    points.append((x2, -1, i))

points.sort()

list = set()

cnt = 0

for x, v, index in points:
    if v == 1:
        if not list:
            cnt += 1
        list.add(index)
    else:
        list.remove(index)

print(cnt)