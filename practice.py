from sortedcontainers import SortedSet

arr = [3, 6, 2, -6, 7, -7, -2, -8]
s = SortedSet()

for elem in arr:
    if elem > 0:                 # 양수인 경우에는
        s.add(elem)              # treeset에 넣어줍니다.
    else:                        # 음수인 경우에는 같거나 큰 최초의 위치를 확인합니다.
        if s.bisect_left(-elem) == len(s):   # 같거나 큰 위치가 없다면
            print(-1, end=" ")               # -1을 출력합니다.
        else:
            print(s[s.bisect_left(-elem)], end=" ") # 있다면 해당 값을 출력합니다.



