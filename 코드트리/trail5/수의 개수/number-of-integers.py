# 9분 5초

n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

def lower_bound(target):
    left = 0
    right = n - 1
    mid_idx = n

    while(left <= right):
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid - 1
            mid_idx = min(mid_idx, mid)
        else:
            left = mid + 1

    return mid_idx

def upper_bound(target):
    left = 0
    right = n - 1
    mid_idx = n

    while(left <= right):
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid - 1
            mid_idx = min(mid_idx, mid)
        else:
            left = mid + 1

    return mid_idx

for elem in queries:
    print(upper_bound(elem)-lower_bound(elem))