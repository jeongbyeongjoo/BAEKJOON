# 23분

K, N = map(int, input().split())
arr = []

def print_arr():
    for elem in arr:
        print(elem, end=' ')
    print()

def choose(num):
    if num == N:
        print_arr()
        return

    for i in range(1, K+1):
        if len(arr) >= 2 and arr[-1] == i and arr[-2] == i:
            continue
        else:
            arr.append(i)
            choose(num+1)
            arr.pop()

choose(0)
