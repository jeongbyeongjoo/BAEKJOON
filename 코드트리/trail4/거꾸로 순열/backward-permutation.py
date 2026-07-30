# 2분 55초

N = int(input())

arr = []
visited = [False]*(N+1)

def print_arr():
    for elem in arr:
        print(elem, end=" ")
    print()

def choose(idx):
    if idx == N+1:
        print_arr()
        return

    for i in range(N, 0, -1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)

            choose(idx+1)

            visited[i] = False
            arr.pop()

choose(1)