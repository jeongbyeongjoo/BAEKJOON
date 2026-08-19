# 7분 17초

n, m = map(int, input().split())

coin = list(map(int, input().split()))

INT_MIN = float('-inf')

dp = [INT_MIN]*(m+1)

dp[0] = 0 

for i in range(1, m+1):
    for j in range(n):
        if i >= coin[j]:
            dp[i] = max(dp[i], dp[i-coin[j]] + 1)

if dp[m] == INT_MIN:
    print(-1)
else:
    print(dp[m])