# 3분 35초

n =  int(input())

s = set()

for _ in range(n):
    instruction, num = input().split()
    if instruction ==  "add":
        s.add(num)
    elif instruction ==  "remove":
        s.remove(num)
    elif instruction ==  "find":
        if num in s:
            print('true')
        else:
            print('false')