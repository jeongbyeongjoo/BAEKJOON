# 11분 25초

n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]


for elem in queries:
    right = len(arr) - 1
    left = 0
    while (left <= right):
        mid = (right + left) // 2
        if arr[mid] == elem:
            print(mid+1)
            break
        elif arr[mid] > elem:
            right = mid -1
        elif arr[mid] < elem:
            left = mid + 1
    if left > right:
        print(-1)
    