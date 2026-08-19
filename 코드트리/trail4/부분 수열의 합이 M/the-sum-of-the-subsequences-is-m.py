n, m = map(int, input().split())
A = list(map(int, input().split()))

INT_MAX = float('inf')

dp = [INT_MAX]*(m+1)

A.sort()

dp[0] = 0
for j in range(n):
    for i in range(m, -1, -1):
        if i >= A[j]:
            dp[i] = min(dp[i], dp[i-A[j]] + 1)

if dp[-1] == INT_MAX:
    print(-1)
else:
    print(dp[-1])
