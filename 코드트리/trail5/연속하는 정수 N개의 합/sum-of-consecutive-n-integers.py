# 13분 58초

n, m = map(int, input().split())
arr = list(map(int, input().split()))

j = 0
cnt = 0
sum = 0

for i in range(n):
    while j < n and sum < m:
        sum += arr[j]
        j += 1
    if sum == m:
        cnt += 1
    sum -= arr[i] 

print(cnt)
    