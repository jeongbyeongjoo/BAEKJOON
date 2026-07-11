import sys

INT_MAX = sys.maxsize
sum = 0

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
for i in range(1, n-1):
    for j in range(n-1):
        if (i == j+1):
            sum += abs(x[j]-x[j+2]) + abs(y[j]-y[j+2])
        elif (i == j):
            continue
        else:
            sum += abs(x[j]-x[j+1]) + abs(y[j]-y[j+1])
    if INT_MAX > sum:
        INT_MAX = sum
    sum = 0

print(INT_MAX)