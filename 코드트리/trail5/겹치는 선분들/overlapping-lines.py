# 42분 22초
# 해설 코드가 더 깔끔

n, k = map(int, input().split())

points = []

x, direction = input().split()
x = int(x)

if direction == 'R':
    points.append((0, 1))
    points.append((x, -1))
    prev_x = x
else:
    points.append((-x, 1))
    points.append((0, -1))
    prev_x = -x

for i in range(1, n):
    x, direction = input().split()
    x = int(x)

    if direction == 'R':
        points.append((prev_x, 1))
        points.append((prev_x + x, -1))
        prev_x = prev_x + x
    else:
        points.append((prev_x - x, 1))
        points.append((prev_x, -1))
        prev_x = prev_x - x

points.sort()
sum = 0
ans = 0
left = 0
right = 0
flag = False

for x, cnt in points:
    sum += cnt

    if sum >= k and not flag:
        left = x
        flag = True

    if sum < k and flag:
        right = x
        ans += right - left
        flag = False

print(ans)