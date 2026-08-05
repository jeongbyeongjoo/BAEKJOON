# 5분 4초

N, M = map(int, input().split())

d1 = dict()
d2 = dict()

for i in range(1, N+1):
    s = input()
    d1[s] = i
    d2[str(i)] = s

for _ in range(M):
    s = input()
    if s in d1:
        print(d1[s])
    elif s in d2:
        print(d2[s])