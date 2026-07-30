# 4분 16초

N, M = map(int, input().split())

arr = []

def print_arr():
    for elem in arr:
        print(elem+1, end=" ")
    print()

def choose(curr_num, cnt):
    if curr_num == N:
        if cnt == M:
            print_arr()
        return

    arr.append(curr_num)
    choose(curr_num+1, cnt+1)
    arr.pop()

    choose(curr_num+1, cnt)

choose(0, 0)