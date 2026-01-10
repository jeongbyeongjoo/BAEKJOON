import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    data = input().strip()

    stack = []
    result = 'YES'

    for i in range(len(data)):
        if (data[i] == '('):
            stack.append(data[i])
        else:
            if (len(stack) > 0):
                stack.pop()
            else:
                result = 'NO'
                break
    if (len(stack) > 0):
        result = 'NO'
    
    print(result)