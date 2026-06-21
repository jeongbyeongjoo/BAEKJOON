# 9분 48초

n = int(input())
arr = list(map(int, input().split()))

ans = 0

for i in range(n-1):
    if arr[i] == 0:
        for j in range(0, 3):
            if i+j < n:
                if arr[i+j] == 0:
                    arr[i+j] = 1
                else:
                    arr[i+j] = 0
        ans += 1

if arr[-1] == 0:
    print(-1)
else:
    print(ans)