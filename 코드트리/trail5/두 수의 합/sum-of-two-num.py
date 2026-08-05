# 23분 9초

N, K = map(int, input().split())

arr = list(map(int, input().split()))

d = dict()

for elem in arr:
    if elem not in d:
        d[elem] = 1
    else:
        d[elem] += 1

cnt = 0

for elem in arr:
    if K - elem in d:
        if K - elem == elem:
            d[elem] -= 1
            cnt += d[elem]
        else:
            if d[K-elem] > 1:
                cnt += d[K-elem]/2
            else:
                cnt += 0.5

print(int(cnt))
