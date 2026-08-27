# 5분 48초

import heapq

n = int(input())

pq = []

for i in range(n):
    instruction = input().split()
    if instruction[0] == 'push':
        heapq.heappush(pq, int(instruction[1])*-1)
    elif instruction[0] == 'size':
        print(len(pq))
    elif instruction[0] == 'empty':
        if pq:
            print(0)
        else:
            print(1)
    elif instruction[0] == 'pop':
        print(-heapq.heappop(pq))
    elif instruction[0] == 'top':
        print(-pq[0])
