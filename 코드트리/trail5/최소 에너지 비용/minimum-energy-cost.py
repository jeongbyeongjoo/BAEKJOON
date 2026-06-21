n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

list = [0]* (n-1)

list[0] = cost[0]

for i in range(1, n-1):
    list[i] = min(list[i-1], cost[i])

sum = 0
for i in range(n-1):
    sum += dist[i] * list[i]

print(sum)