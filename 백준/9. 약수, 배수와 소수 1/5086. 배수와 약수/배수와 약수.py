while(1):
    A, B = map(int, input().split())
    if A == 0:
        break
    if A > B:
        if int(A / B) == float(A / B):
            print('multiple')
        else:
            print('neither')
    else:
        if int(B / A) == float(B / A):
            print('factor')
        else:
            print('neither')