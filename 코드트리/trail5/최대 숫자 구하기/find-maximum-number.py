from sortedcontainers import SortedSet

n, m = map(int, input().split())
queries = list(map(int, input().split()))

SortedSet = SortedSet()

for i in range(1, m+1):
    SortedSet.add(i)

for elem in queries:
    SortedSet.remove(elem)
    print(SortedSet[-1])

