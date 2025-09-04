N, M = map(int, input().split())

set_A = set(input().split())
set_B = set(input().split())

A_sub_B = set_A.difference(set_B)
B_sub_A = set_B.difference(set_A)

print(len(A_sub_B) + len(B_sub_A))