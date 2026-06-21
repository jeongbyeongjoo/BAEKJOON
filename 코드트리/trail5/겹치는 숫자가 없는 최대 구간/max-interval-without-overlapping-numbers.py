n = int(input())
arr = list(map(int, input().split()))

j = 0
cnt = [0] * 100001
MIN_INT = float('-inf')
max_int = MIN_INT

for i in range(n):
    while j < n and cnt[arr[j]] < 1:
        cnt[arr[j]] += 1
        j += 1
    
    max_int = max(max_int, j-i)

    cnt[arr[i]] -= 1

print(max_int)