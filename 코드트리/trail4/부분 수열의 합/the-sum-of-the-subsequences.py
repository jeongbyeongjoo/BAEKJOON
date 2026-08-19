n, m = map(int, input().split())
A = list(map(int, input().split()))

INT_MAX = float('inf')
dp = [INT_MAX for _ in range(m+1)]

dp[0] = 0

for elem in A:
    for i in range(m, -1, -1):
        if i >= elem:
            dp[i] = min(dp[i], dp[i-elem] + 1)

if dp[m] == INT_MAX:
    print('No')
else:
    print('Yes')
