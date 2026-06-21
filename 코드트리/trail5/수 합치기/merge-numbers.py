# 9분 34초
import heapq

n = int(input())
arr = list(map(int, input().split()))

pq = []

for elem in arr:
    heapq.heappush(pq, elem)

sum = 0
cnt = 0

while pq:
    data1 = heapq.heappop(pq)
    data2 = heapq.heappop(pq)
    sum = data1 + data2
    cnt += sum
    if len(pq) >= 1:
        heapq.heappush(pq, sum)
    else:
        break

print(cnt)
