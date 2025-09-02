N = int(input())
arr = list(map(int, input().split()))
d = {x: 0 for x in arr}

count = 0

for key in d:
    for i in range(1, key+1):
        if key % i == 0:
            d[key] += 1    

print(list(d.values()).count(2))
