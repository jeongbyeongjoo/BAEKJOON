n = int(input())
arr = list(map(int, input().split()))

dp = [0]*(n+1)

for i in range(n):
    for j in range(i):
        if j + arr[j] >= i :
            if i == 1 or dp[i-1] != 0:
                dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
