n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
arr = []
max_val = float('-inf')

# Please write your code here.
def choose(curr_num):
    if curr_num == n:
        global max_val
        sum = [0 for i in range(k+1)]
        count = 0

        for i in range(len(nums)):
            sum[arr[i]] += nums[i]    

        for i in range(1, len(sum)):
            if sum[i] >= m - 1:
                count += 1

        if count > max_val:
            max_val = count

        return

    for i in range(1, k+1):
        arr.append(i)
        choose(curr_num+1)
        arr.pop()

choose(0)
print(max_val)
