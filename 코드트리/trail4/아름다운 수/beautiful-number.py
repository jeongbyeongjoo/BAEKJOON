# 11분 27초

import sys

sys.setrecursionlimit(1000000)

N = int(input())

cnt = 0

def choose(idx):
    global cnt
    if idx == N:
        cnt += 1
        return
    elif idx > N:
        return

    for i in range(1, 5):
        choose(idx+i)

choose(0)

print(cnt)