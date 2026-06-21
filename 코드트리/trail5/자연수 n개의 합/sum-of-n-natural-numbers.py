# 13분
s = int(input())

left = 0
right = 10000000000
# 이거 0으로 하는게 좋을듯 아예 max를 다 통과해도 -1이 되는 상황이 있을 수 될수도 있기 때문
mid_num = 0

while left <= right:
    mid = (left + right) // 2
    if mid * (mid + 1) // 2 <= s:
        left = mid + 1
        mid_num = max(mid_num, left)
    else:
        right = mid - 1

print(mid_num-1)