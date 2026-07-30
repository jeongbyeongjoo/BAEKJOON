n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

dir_arr = [[],[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
max_val = float('-inf')

def choose(curr_cnt, r, c):
    if find_maxval(move_dir[r][c], r, c, num[r][c]) == False:
        global max_val
        if curr_cnt > max_val:
            max_val = curr_cnt
        return 
    
    maxval_list = find_maxval(move_dir[r][c], r, c, num[r][c])
    for i in range(len(maxval_list)):
        choose(curr_cnt+1, maxval_list[i][0], maxval_list[i][1])

def find_maxval(direction, r, c, current_num):
    maxval_list = []
    for i in range(1, n):
        if cal_range(r + dir_arr[direction][0]*i, c + dir_arr[direction][1]*i):
            if num[r + dir_arr[direction][0]*i][c + dir_arr[direction][1]*i] > current_num:
                maxval_list.append([r + dir_arr[direction][0]*i, c + dir_arr[direction][1]*i])
    if len(maxval_list) == 0:
        return False
    else: 
        return maxval_list

def cal_range(r, c):
    return 0 <= r < n and 0 <= c < n

choose(0, r-1, c-1)

print(max_val)
