import sys
from collections import deque
        
n = int(sys.stdin.readline())

dq = deque()

for i in range(n):
    data = sys.stdin.readline().split()
    if '1' == data[0]:
        dq.appendleft(int(data[-1]))
    elif '2' == data[0]:
        dq.append(int(data[-1]))
    elif '3' == data[0]:
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif '4' == data[0]:
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif '5' == data[0]:
        print(len(dq))
    elif '6' == data[0]:
        if not dq:
            print(1)
        else:
            print(0)
    elif '7' == data[0]:
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif '8' == data[0]:
        if dq:
            print(dq[-1])
        else:
            print(-1)