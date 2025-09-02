N, k = map(int, input().split())

arr = list(map(int, input().split()))

arr_sorted = sorted(arr, reverse=True)

print(arr_sorted[k-1])