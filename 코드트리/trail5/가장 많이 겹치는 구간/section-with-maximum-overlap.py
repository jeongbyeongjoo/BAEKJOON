# 15분

n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

points = []

for x1, x2 in intervals:
    points.append((x1, +1))
    points.append((x2, -1))

points.sort()

sum = 0
sum_list = []

for x, v in points:
    sum += v
    sum_list.append(sum)

print(max(sum_list))