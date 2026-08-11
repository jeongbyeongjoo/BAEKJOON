# 4분 5초

n, k = map(int, input().split())
arr = list(map(int, input().split()))

sum = [0]*(n+1)

sum[0] = 0
for i in range(1, n+1):
    sum[i] = sum[i-1] + arr[i-1]

max_int = float('-inf')
for i in range(k, n+1):
    max_int = max(max_int, sum[i] - sum[i - k])

print(max_int)