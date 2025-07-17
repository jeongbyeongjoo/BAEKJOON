arr = []
max = 0
row, column = 0, 0

for i in range(9):
    arr.append(list(map(int, input().split())))
    
for i in range(9):
    for j in range(9):
        if max < arr[i][j]:
            max = arr[i][j]
            row, column = i, j
    
print(max)
print(row+1, column+1)