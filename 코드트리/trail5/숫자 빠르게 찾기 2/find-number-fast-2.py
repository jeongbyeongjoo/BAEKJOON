from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

SORTED_SET = SortedSet(arr)

for elem in queries:
    data = SORTED_SET.bisect_left(elem)
    if data == len(SORTED_SET):
        print(-1)
    else:
        print(SORTED_SET[data])

