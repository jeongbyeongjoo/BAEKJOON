N = int(input())
level = 1
idx = 1

while(1):
    if N > idx:
        idx += level * 6
        level += 1
    else:
        break

print(level)