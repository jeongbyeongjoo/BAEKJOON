import heapq

N = int(input())
commands = []

for _ in range(N):
    line = input().split()
    if line[0] == "push":
        commands.append((line[0], int(line[1])))
    else:
        commands.append((line[0],))

heap = []

for elem in commands:
    if elem[0] == 'push':
        heapq.heappush(heap, -elem[1])
    elif elem[0] == 'pop':
        print(-heapq.heappop(heap))
    elif elem[0] == 'size':
        print(len(heap))
    elif elem[0] == 'empty':
        if not heap:
            print(1)
        else:
            print(0)
    elif elem[0] == 'top':
        print(-heap[0])
