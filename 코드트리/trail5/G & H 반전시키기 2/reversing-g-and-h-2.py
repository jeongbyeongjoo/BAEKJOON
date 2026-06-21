# 16분 17초

n = int(input())
a = input()
b = input()

ans = 0

list_a = []
list_b = []

for i in range(n):
    if a[i] == 'H':
        list_a.append(1)
    else:
        list_a.append(0)
    if b[i] == 'H':
        list_b.append(1)
    else:
        list_b.append(0)

for i in range(n-1, -1, -1):
    if list_a[i] != list_b[i]:
        for j in range(i+1):
            if list_a[j] == 1:
                list_a[j] = 0
            else:
                list_a[j] = 1
        ans += 1

print(ans)