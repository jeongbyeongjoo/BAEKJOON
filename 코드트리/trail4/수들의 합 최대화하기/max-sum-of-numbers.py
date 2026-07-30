n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n

int_max = 0

def choose(curr_row, sum):
    global int_max
    if curr_row == n:
        int_max = max(int_max, sum)
        return 
    
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        choose(curr_row+1, sum + grid[curr_row][i])
        visited[i] = False
        
choose(0, 0)
print(int_max)
