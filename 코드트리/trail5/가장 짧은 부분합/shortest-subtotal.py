n, s = map(int, input().split())
arr = list(map(int, input().split()))

INT_MAX = float('inf')

sum = 0
j = 0
min_cnt = INT_MAX

for i in range(n):
    while j < n and sum < s:
        sum += arr[j]
        j += 1
    if sum >= s:
        min_cnt = min(min_cnt, j-i)

    sum -= arr[i]

if min_cnt == float('inf'):
    print(-1)
else:
    print(min_cnt)