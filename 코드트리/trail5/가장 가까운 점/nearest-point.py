import heapq

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

heap = []

for x, y in points:
    heapq.heappush(heap, (x+y, x, y))

for i in range(m):
    _, x, y = heapq.heappop(heap)
    x += 2
    y += 2
    heapq.heappush(heap, (x + y, x, y))

_, x, y = heapq.heappop(heap)

print(x, y)


