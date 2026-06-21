n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

def solve(num):
    cnt = 0
    for elem in arr:
        data = elem // num
        cnt += data

    return m <= cnt

left = 1
right = 100000
mid_num = 0

while left <= right:
    mid = (left+right)//2
    if solve(mid):
        left = mid + 1
        mid_num = max(mid_num, mid)
    else:
        right = mid -1

print(mid_num)