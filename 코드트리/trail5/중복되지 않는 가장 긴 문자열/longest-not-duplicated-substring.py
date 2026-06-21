# 13분 45초

word = input()
n = len(word)

cnt = [0] * 1000
j = 0
INT_MIN = float('-inf')
ans = INT_MIN

for i in range(n):
    while j < n and cnt[ord(word[j])] < 1:
        cnt[ord(word[j])] += 1
        j += 1
    cnt[ord(word[i])] -= 1
    ans = max(ans, j-i)

print(ans)
    



