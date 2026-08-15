n, s = map(int, input().split())

arr = list(map(int, input().split()))

sum = 0
j = 0
min_int = 100001
for i in range(n):
    while j < n and sum < s:
        sum += arr[j]
        j += 1

    if j < n:
        min_int = min(min_int, j - i)
    sum -= arr[i]

if min_int == 100001:
    print(-1)
else:
    print(min_int)