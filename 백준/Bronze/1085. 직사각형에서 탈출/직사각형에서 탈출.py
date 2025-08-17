x, y, w, h = list(map(int, input().split()))

arr = [w-x, x, h-y, y]

print(min(arr))