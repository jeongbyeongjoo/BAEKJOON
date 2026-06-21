# 4분 1

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

sum = 0

for i in range(n-1, -1, -1):
    data = k // coins[i]
    sum += data
    k = k - data*coins[i]
    
print(sum)