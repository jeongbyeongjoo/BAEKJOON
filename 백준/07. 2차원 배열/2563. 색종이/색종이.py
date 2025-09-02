n = int(input())
arr = []
x_max = 0
y_max = 0
sum = 0

for i in range(n):
    data = list(map(int, input().split()))
    arr.append(data)
    if data[0] > x_max:
        x_max = data[0]
    if data[1] > y_max:
        y_max = data[1]

matrix = [[0 for _ in range(y_max+10)] for _ in range(x_max+10)]
   
for i in range(n):    
    for j in range(arr[i][0], arr[i][0]+10):
        for k in range(arr[i][1], arr[i][1]+10):
            matrix[j][k] = 1
   
for row in matrix:
    for data in row:
        sum += data
    
print(sum)


    
