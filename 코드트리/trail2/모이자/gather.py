# 6분

n = int(input())
A = list(map(int, input().split()))

INT_MAX = float('inf')
answer = INT_MAX

for i in range(n):
    sum = 0
    for j in range(n):
        if i == j:
            continue
        sum += A[j] * abs(j-i)
    answer = min(answer, sum)

print(answer)
