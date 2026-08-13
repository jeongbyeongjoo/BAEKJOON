import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))

heap = []

for elem in arr:
    heapq.heappush(heap, -elem)

for i in range(m):
    heapq.heappush(heap, heapq.heappop(heap)+1)

print(-heapq.heappop(heap))

