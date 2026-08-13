import heapq

n = int(input())
x = [int(input()) for _ in range(n)]

heap = []

for elem in x:
    if elem != 0:
        heapq.heappush(heap, elem)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
