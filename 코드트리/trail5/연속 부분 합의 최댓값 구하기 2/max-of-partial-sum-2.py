# 5분 8초

n = int(input())
a = list(map(int, input().split()))

max_int = float('-inf')
sum = 0

for elem in a:
    sum += elem

    max_int = max(max_int, sum)

    if sum < 0:
        sum = 0

print(max_int)