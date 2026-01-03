import math

A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())

lcm = B1 * B2 // math.gcd(B1, B2)
A3 = int(lcm/B1*A1 + lcm/B2*A2)
B3 = int(lcm)

if A3 % math.gcd(A3, B3)==0 and B3 % math.gcd(A3,B3)==0:
    gcd = math.gcd(A3, B3)
    A3 = A3/gcd
    B3 = B3/gcd   
    
print(int(A3), int(B3))