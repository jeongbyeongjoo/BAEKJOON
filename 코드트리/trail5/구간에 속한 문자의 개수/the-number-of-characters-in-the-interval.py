n, m, k = map(int, input().split())

grid = ['0' * (m+1)] + ['0' + input() for _ in range(n)]

queries = [tuple(map(int, input().split())) for _ in range(k)]

sum_arr = [[[0]*(m+1) for _ in range(n+1)] for _ in range(3)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if grid[i][j] == 'a':
            sum_arr[0][i][j] = sum_arr[0][i-1][j] + sum_arr[0][i][j-1] - sum_arr[0][i-1][j-1] + 1
            sum_arr[1][i][j] = sum_arr[1][i-1][j] + sum_arr[1][i][j-1] - sum_arr[1][i-1][j-1]
            sum_arr[2][i][j] = sum_arr[2][i-1][j] + sum_arr[2][i][j-1] - sum_arr[2][i-1][j-1]
        elif grid[i][j] == 'b':
            sum_arr[0][i][j] = sum_arr[0][i-1][j] + sum_arr[0][i][j-1] - sum_arr[0][i-1][j-1]
            sum_arr[1][i][j] = sum_arr[1][i-1][j] + sum_arr[1][i][j-1] - sum_arr[1][i-1][j-1] + 1
            sum_arr[2][i][j] = sum_arr[2][i-1][j] + sum_arr[2][i][j-1] - sum_arr[2][i-1][j-1]
        elif grid[i][j] == 'c':
            sum_arr[0][i][j] = sum_arr[0][i-1][j] + sum_arr[0][i][j-1] - sum_arr[0][i-1][j-1]
            sum_arr[1][i][j] = sum_arr[1][i-1][j] + sum_arr[1][i][j-1] - sum_arr[1][i-1][j-1]
            sum_arr[2][i][j] = sum_arr[2][i-1][j] + sum_arr[2][i][j-1] - sum_arr[2][i-1][j-1] + 1
        
for r1, c1, r2, c2 in queries:
    print(sum_arr[0][r2][c2] - sum_arr[0][r1-1][c2] - sum_arr[0][r2][c1-1] + sum_arr[0][r1-1][c1-1], end=' ')
    print(sum_arr[1][r2][c2] - sum_arr[1][r1-1][c2] - sum_arr[1][r2][c1-1] + sum_arr[1][r1-1][c1-1], end=' ')
    print(sum_arr[2][r2][c2] - sum_arr[2][r1-1][c2] - sum_arr[2][r2][c1-1] + sum_arr[2][r1-1][c1-1], end=' ')
    print()

