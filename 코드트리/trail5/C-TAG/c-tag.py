n, m = map(int, input().split())

A = [input() for _ in range(n)]
B = [input() for _ in range(n)]

cnt = 0

for i in range(m-2):
    for j in range(i+1, m-1):
        for k in range(j+1, m):
            A_list = [A[l][i] + A[l][j] + A[l][k] for l in range(n)]
            B_list = [B[l][i] + B[l][j] + B[l][k] for l in range(n)]
            
            SET = set(A_list)

            flag = 0
            
            for elem in B_list:
                if elem in SET:
                    flag = 1
            
            if not flag:
                cnt += 1

print(cnt)
