N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

list = [(w[i], v[i]) for i in range(N)]
list.sort()

INT_MIN = float('-inf')

dp = [INT_MIN for i in range(M+1)]

dp[0] = 0

for w, v in list:
    for i in range(M, -1, -1):
        if i >= w:
            dp[i] = max(dp[i], dp[i-w] + v)

print(max(dp))
