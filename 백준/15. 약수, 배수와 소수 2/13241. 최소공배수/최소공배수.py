import sys
import math

input = sys.stdin.readline
write = sys.stdout.write

A, B = map(int, input().split())

write(str(A * B // math.gcd(A, B)))