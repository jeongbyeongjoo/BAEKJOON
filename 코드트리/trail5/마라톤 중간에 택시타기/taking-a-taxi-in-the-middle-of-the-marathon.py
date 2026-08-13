INT_MAX = float('inf')

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

Lx = [0]*n
Rx = [0]*n
Ly = [0]*n
Ry = [0]*n

answer = INT_MAX

for i in range(1, n):
    Lx[i] = abs(x[i] - x[i-1]) + Lx[i-1]
    Ly[i] = abs(y[i] - y[i-1]) + Ly[i-1]

for i in range(n-2, -1, -1 ):
    Rx[i] = abs(x[i+1] - x[i]) + Rx[i+1]
    Ry[i] = abs(y[i+1] - y[i]) + Ry[i+1]

for i in range(0, n - 2):
    data_x = Lx[i] + abs(x[i+2] - x[i]) + Rx[i+2]
    data_y = Ly[i] + abs(y[i+2] - y[i]) + Ry[i+2]
    answer = min(answer, data_x + data_y)

print(answer)
