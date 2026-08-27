# 8분 32초

n = int(input())

def solve(mid):
    return mid - mid//3 - mid//5 + mid//15

left = 0
right = 10**18
mid_num = 10**18

while left <= right:
    mid = (left + right) // 2
    if solve(mid) >= n:
        mid_num = min(mid_num, mid)
        right = mid -1 
    else:
        left = mid + 1

print(mid_num)