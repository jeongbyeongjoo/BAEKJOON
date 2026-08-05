from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

SORTED_SET = SortedSet(arr)

INT_MIN = float('inf')
result = INT_MIN

for elem in arr:
    min_idx = SORTED_SET.bisect_left(m+elem)
    if min_idx != len(SORTED_SET):
        result = min(result, SORTED_SET[min_idx]-elem)
    
    max_idx = SORTED_SET.bisect_right(elem-m)-1
    if max_idx >= 0:
        result = min(result, elem - SORTED_SET[max_idx])

if result == float('inf'):
    print(-1)
else:
    print(result)
