# 6분 14초

N = int(input())

d = dict()

for _ in range(N):
    instruction = input().split()

    if instruction[0] == "add":
        k = instruction[1]
        v = instruction[2]
        d[k] = v
    elif instruction[0] == "remove":
        k = instruction[1]
        d.pop(k)
    elif instruction[0] == "find":
        k = instruction[1]        
        if k in d:
            print(d[k])
        else:
            print(None)