N = int(input())
B = [input() for _ in range(N)]

A_LEFT = [[0]*3 for _ in range(N)]
A_RIGHT = [[0]*3 for _ in range(N)]

INT_MIN = float('-inf')
answer = INT_MIN

for i in range(N):
    for j in range(3):
        if i == 0:
            A_LEFT[i][j] = 0
            continue
        A_LEFT[i][j] = A_LEFT[i-1][j]
    if B[i] == 'H': # 주먹
        A_LEFT[i][2] += 1
    elif B[i] == 'S': # 가위
        A_LEFT[i][0] += 1
    elif B[i] == 'P': # 보
        A_LEFT[i][1] += 1
        
for i in range(len(B)-1, -1, -1):
    for j in range(3):
        if i == len(B) - 1:
            A_RIGHT[len(B)-1][j] = 0
            continue
        A_RIGHT[i][j] = A_RIGHT[i+1][j]
    if B[i] == 'H': # 주먹
        A_RIGHT[i][2] += 1
    elif B[i] == 'S': # 가위
        A_RIGHT[i][0] += 1
    elif B[i] == 'P': # 보
        A_RIGHT[i][1] += 1

for i in range(N-1):
    for j in range(3):
        data = A_LEFT[i][j] + A_RIGHT[i+1][j-1]
        data2 = A_LEFT[i][j] + A_RIGHT[i+1][j]
        data3 = A_LEFT[i][j] + A_RIGHT[i+1][j-2]
        answer = max(answer, data, data2, data3)

print(answer)

