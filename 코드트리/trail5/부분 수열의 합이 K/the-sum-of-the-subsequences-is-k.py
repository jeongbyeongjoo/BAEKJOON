# 10분 25초

n, k = map(int, input().split())

arr = [0] + list(map(int, input().split()))

sum_arr = [0]*(n+1)

sum_arr[0] = 0

for i in range(1, n+1):
    sum_arr[i] = sum_arr[i-1] + arr[i]

sum = 0
cnt = 0

for i in range(n+1):
    for j in range(i+1, n+1):
        sum = sum_arr[j] - sum_arr[i]
        if sum == k:
            cnt += 1
            break
        elif sum > k:
            break

print(cnt)