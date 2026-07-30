# 3분 16초

N = int(input())

arr = []
visited = [False]*(N+1)

def print_arr():
    for elem in arr:
        print(elem, end=" ")
    print()

def choose(idx):
    if idx == N + 1:
        print_arr()
        return

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)

            choose(idx+1)

            arr.pop()
            visited[i] = False

choose(1)
