N = int(input())
arr_N = list(map(int, input().split()))
dict_N = {x:1 for x in arr_N}

M = int(input())
arr_M = list(map(int, input().split()))

for i in range(M):
    print(dict_N.get(arr_M[i], 0), end=" ")
    


    