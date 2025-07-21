N = int(input())
data = 3

for i in range(N):
    result = data*data
    data += data-1
    
print(result)