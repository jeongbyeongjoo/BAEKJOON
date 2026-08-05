from sortedcontainers import SortedSet

INT_MIN = float('inf')

n = int(input())
queries = list(map(int, input().split()))

SORTEDSET = SortedSet()
SORTEDSET.add(0)

for elem in queries:
    SORTEDSET.add(elem)
    right = SORTEDSET.bisect_right(elem)
    left = right - 1
    if right == len(SORTEDSET):
        data = SORTEDSET[left] - SORTEDSET[left - 1]
    else:
        data = min(SORTEDSET[right] - SORTEDSET[left], SORTEDSET[left] - SORTEDSET[left-1])

    if INT_MIN > data:
        INT_MIN = data
    
    print(INT_MIN)


    
