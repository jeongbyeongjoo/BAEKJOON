# 9분 40초
# 이렇게 하니깐 시간초과 남
# for elem in arr:
#     ans = ans + elem

# print(ans)

from functools import cmp_to_key

n = int(input())
arr = [int(input()) for _ in range(n)]

def compare(x, y):
    x = str(x)
    y = str(y)
    if x+y > y+x:
        return -1
    if y+x > x+y:
        return 1
    return 0

arr.sort(key = cmp_to_key(compare))

ans = ""

for elem in arr:
    print(elem, end="")

