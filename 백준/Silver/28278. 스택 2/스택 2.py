import sys

input = sys.stdin.readline

n = int(input())

stack = []

for i in range(n):
    data = list(map(int, input().split()))
    if (data[0] == 1):
        stack.append(data[1])
    elif (data[0] == 2):
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif (data[0] == 3):
        print(len(stack))
    elif (data[0] == 4):
        if len(stack) > 0:
            print(0)
        else:
            print(1)            
    elif (data[0] == 5):
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
