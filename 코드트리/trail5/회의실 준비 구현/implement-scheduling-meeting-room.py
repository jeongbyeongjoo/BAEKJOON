# 12분 59초

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

meetings.sort(key = lambda x:x[1])

list = []

list.append(meetings[0])

for i in range(1, n):
    if list[-1][1] <= meetings[i][0]:
        list.append(meetings[i])

print(len(list))