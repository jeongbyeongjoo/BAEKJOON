n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 폭탄 인덱스를 저장하는 배열
boom_arr = []
max = float('-inf')

# Please write your code here.
def choose(current_number):
    global max

    if current_number == len(boom_arr):
        count = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
        
        if count > max:
            max = count

        return 
    
    row, col = boom_arr[current_number]

    # 1번 폭탄
    first_boom(row, col, current_number)
    second_boom(row, col, current_number)
    third_boom(row, col, current_number)

# 1번 폭탄
def first_boom(row, col, current_number):
    # 영향을 받는 좌표들
    targets = [(row-2, col), (row-1, col), (row+1, col), (row+2, col)]
    added_positions = []

    for r, c in targets:
        if 0 <= r < n and grid[r][c] == 0: # 원래 0이었던 경우만!
            grid[r][c] = 1
            added_positions.append((r, c)) # 내가 바꿨다고 기록
            
    choose(current_number + 1)

    # [Backtracking] 내가 바꾼 것만 다시 0으로 복구
    for r, c in added_positions:
        grid[r][c] = 0
    
# 2번 폭탄
def second_boom(row, col, current_number):
    # 영향을 받는 좌표들 (상, 하, 좌, 우)
    targets = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    added_positions = []

    # 격자 안에 있는 경우에만 1로 바꾸고, 나중에 되돌리기 위해 기록
    for r, c in targets:
        if 0 <= r < n and 0 <= c < n and grid[r][c] == 0: # 원래 0이었던 경우만!
            grid[r][c] = 1
            added_positions.append((r, c)) # 내가 바꿨다고 기록

    choose(current_number + 1)
    
    # [Backtracking] 내가 바꾼 것만 다시 0으로 복구
    for r, c in added_positions:
        grid[r][c] = 0

# 3번 폭탄
def third_boom(row, col, current_number):
    # 영향을 받는 좌표들 (대각선 4방향)
    targets = [(row-1, col-1), (row-1, col+1), (row+1, col-1), (row+1, col+1)]
    added_positions = []

    for r, c in targets:
        if 0 <= r < n and 0 <= c < n and grid[r][c] == 0: # 원래 0이었던 경우만!
            grid[r][c] = 1
            added_positions.append((r, c)) # 내가 바꿨다고 기록
            
    choose(current_number + 1)
    
    # [Backtracking] 내가 바꾼 것만 다시 0으로 복구
    for r, c in added_positions:
        grid[r][c] = 0

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            boom_arr.append((i, j))

choose(0)

print(max)
