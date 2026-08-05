from sortedcontainers import SortedSet

n = int(input())
P, L = [], []
for _ in range(n):
    p, l = map(int, input().split())
    P.append(p)
    L.append(l)

m = int(input())
commands = []
for _ in range(m):
    cmd = input().split()
    if cmd[0] == "rc":
        commands.append((cmd[0], int(cmd[1])))
    else:
        commands.append((cmd[0], int(cmd[1]), int(cmd[2])))

S = SortedSet()

for i in range(n):
    S.add((L[i], P[i]))

for elem in commands:
    if elem[0] == 'ad':
        S.add((elem[2], elem[1]))
    elif elem[0] == 'sv':
        S.remove((elem[2], elem[1]))
    elif elem[0] == 'rc':
        if elem[1] == 1:
            print(S[-1][1])
        else: # -1일 때
            print(S[0][1])


