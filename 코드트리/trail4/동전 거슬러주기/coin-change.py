# 7분 39초

n, m = map(int, input().split())

cost = [0] + list(map(int, input().split()))

INT_MAX = float('inf')

dp = [INT_MAX]*(m+1)
dp[0] = 0

for i in range(1, m+1):
    for j in range(1, n+1):
        if i >= cost[j]:
            dp[i] = min(dp[i], dp[i - cost[j]] + 1)

if dp[m] == INT_MAX:
    print(-1)
else:
    print(dp[m])