# 4분 20초

n = int(input())
numbers = list(map(int, input().split()))

INT_MIN = float('-inf')
answer = INT_MIN

for i in range(n):
    for j in range(i+2, n):
        sum = numbers[i] + numbers[j]
        answer = max(answer, sum)

print(answer)