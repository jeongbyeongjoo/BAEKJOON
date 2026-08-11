n, k = map(int, input().split())
arr = [[0] * (n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
sum_arr = [[0] * (n+1) for _ in range(n+1)]

INT_MIN = float('-inf')

answer = INT_MIN

for i in range(1, n+1):
    for j in range(1, n+1):
        sum_arr[i][j] = sum_arr[i-1][j] + sum_arr[i][j-1] - sum_arr[i-1][j-1] + arr[i][j]

for i in range(k, n+1):
    for j in range(k, n+1):
        data = sum_arr[i][j] - sum_arr[i-k][j] - sum_arr[i][j-k] + sum_arr[i-k][j-k]
        answer = max(answer, data)

print(answer)
