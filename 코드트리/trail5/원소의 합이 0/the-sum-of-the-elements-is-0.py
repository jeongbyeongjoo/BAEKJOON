n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

dict1 = dict()
dict2 = dict()

cnt = 0
for a in A:
    for b in B:
        if a+b in dict1:
            dict1[a+b] += 1
        else:
            dict1[a+b] = 1

for c in C:
    for d in D:
        if c+d in dict2:
            dict2[c+d] += 1
        else:
            dict2[c+d] = 1

for elem in dict1:
    if -elem in dict2:
        cnt += dict1[elem] * dict2[-elem]

print(cnt)
