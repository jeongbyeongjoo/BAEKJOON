n = int(input())
grid = [list(input()) for _ in range(n)]
start_pos = [0, 0]
end_pos = [0,0]
num_arr = []

int_min = float('inf')

def choose(x, y, target, curr_dis, cnt):
    global int_min
    if target  == len(num_arr):
        if cnt >= 3:
            curr_dis = curr_dis + abs(x-end_pos[0]) + abs(y-end_pos[1])
            int_min = min(curr_dis, int_min)
        return
    
    next_x = num_arr[target][1][0]
    next_y = num_arr[target][1][1]

    dis = abs(x-next_x) + abs(y-next_y)

    # 다음번호로 넘기기
    choose(x, y, target+1, curr_dis, cnt)

    # 이번번호 포함하기
    choose(next_x, next_y, target+1, curr_dis+dis, cnt + 1)

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            start_pos = i, j
        elif grid[i][j] == 'E':
            end_pos = i, j
        elif grid[i][j] != '.':
            num_arr.append((int(grid[i][j]), (i, j)))

num_arr.sort()
# num_arr.append([0, end_pos])

choose(start_pos[0], start_pos[1], 0, 0, 0)

if len(num_arr) < 3:
    int_min = -1

if int_min == float('inf'):
    print(-1)
else:
    print(int_min)
