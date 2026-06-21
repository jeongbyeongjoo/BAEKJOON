# 못품 (그냥 여기 문제는 시험 때 패스하닌게 나을지도...)
# 다시 풀기(삼오무로 푸는 이 로직을 기억해야함)
# is_possible()에 리턴값이랑 n은 입력부분(4)으로 생각해서 서로 비교하게 냅두고
# 실제로 구한는 위치값?을 출력(while문의 left, right로 나오는 숫자)으로 설정(7)
# INT_MAX = float('inf')로 풀면 오류남
n = int(input())

def solve(num):
    sum = num
    sum -= num // 3
    sum -= num // 5
    sum += num // 15

    return n <= sum

left = 1
right = 1000000000000
mid_num = 1000000000000

while left <= right:
    mid = (left + right) // 2
    if solve(mid):
        right = mid - 1
        mid_num = min(mid_num, mid)
    else:
        left = mid + 1

print(mid_num)
