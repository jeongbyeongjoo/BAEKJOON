# 10분 54초
a = list(map(int, input()))
n = len(a)

def solve(a):
    sum = 0
    for i in range(n):
        sum += a[i] * 2 **(n-i-1)
    return sum

max_sum = float('-inf')

for i in range(n):
    if a[i] == 1:
        a[i] = 0
    else:
        a[i] = 1
    max_sum = max(max_sum, solve(a))
    if a[i] == 1:
        a[i] = 0
    else:
        a[i] = 1

print(max_sum)