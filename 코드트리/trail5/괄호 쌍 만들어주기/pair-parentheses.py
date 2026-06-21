# 29분 50초
A = input()

cnt = 0
b = [0] * (len(A)+1)

for i in range(len(A) - 2, -1, -1):
    if A[i] == A[i+1] and A[i] == ')':
        b[i] += b[i+1] + 1
    else:
        b[i] = b[i+1]

for i in range(len(A)-1):
    if A[i] == A[i+1] and A[i] == '(':
            cnt += b[i]

print(cnt)            