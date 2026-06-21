# 14분 10초

N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

list = []

for i in range(N):
    list.append((v[i]/w[i], w[i], v[i]))

list.sort()

ans = 0

for elem in list[::-1]:
    if M - elem[1] >= 0:
        M -= elem[1]
        ans += elem[2]
    else: 
        ans += elem[2]/elem[1]*M
        M = 0

print(f"{ans:.3f}")