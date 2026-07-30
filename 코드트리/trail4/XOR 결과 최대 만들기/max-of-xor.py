# 8분 12초

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr2 = []
max_int = 0

def choose(curr_num, cnt):
    global max_int
    if curr_num == N:
        if cnt == M:
            sum = arr2[0]
            for i in range(1, M):
                sum ^= arr2[i]
            max_int = max(max_int, sum)
        return

    arr2.append(arr[curr_num])
    choose(curr_num+1, cnt+1)
    arr2.pop()

    choose(curr_num+1, cnt)

choose(0, 0)

print(max_int)