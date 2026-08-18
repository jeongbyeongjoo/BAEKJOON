# 8분 54초

n = int(input())

dist = []

for i in range(n):
    row = list(map(int, input().split()))
    dist.append(row)

dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][0] = dist[0][0]

for i in range(1, n):
    dp[0][i] = dp[0][i-1] + dist[0][i] 

for i in range(1, n):
    dp[i][0] = dp[i-1][0] + dist[i][0]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + dist[i][j]

print(dp[n-1][n-1])