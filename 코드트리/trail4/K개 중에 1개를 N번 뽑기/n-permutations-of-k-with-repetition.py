# 5분 33초

K, N = map(int, input().split())
arr = []

def print_arr():
    for i in range(N):
        print(arr[i], end = " ")
    print()

def choose(num):
    if num == N:
        print_arr()
        return

    for i in range(1, K+1):
        arr.append(i)
        choose(num+1)
        arr.pop()

choose(0)