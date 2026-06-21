# 문제 설명이 ㅈ같노
# 17분 48초

N = int(input())
a = input()
b = input()

ans = 0

for i in range(N):
    if a[i] != b[i]:
        ans += 1
    if i >= 1 and a[i] != b[i] and a[i-1] != b[i-1]:
        ans -= 1

print(ans)