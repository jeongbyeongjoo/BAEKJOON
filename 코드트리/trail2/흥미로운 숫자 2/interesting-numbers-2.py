# 18분

X, Y = map(int, input().split())

sum1 = 0
sum2 = 0
ans = 0

for s in range(X, Y+1):
    cnt = [0]*10
    s = str(s)
    for i in range(len(s)):
        cnt[int(s[i])] += 1
    for i in range(10):
        if cnt[i] == 1:
            sum1 += 1
        if cnt[i] == len(s) - 1:
            sum2 += 1
    if sum1 == 1 and sum2 == 1:
        ans += 1
    sum1 = 0
    sum2 = 0

print(ans)