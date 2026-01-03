import sys

input = sys.stdin.readline

n = int(input())

count = 0
i = 1

while(i*i <= n):
    i += 1
    count += 1

print(count)