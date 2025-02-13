def jumps(nums: list[int]) -> int:
    i = 0
    n = len(nums)
    jumps = 0
    while i < n:
        # if i == n-1:
        #     break
        # if nums[i] == 0:
        #     return -1
        # m = 0
        # j = 0
        # for k in range(1, nums[i]+1):
        #     if i+k >= n-1:
        #         j = i+k
        #         break
        #     if nums[i+k] + k > m:
        #         m = nums[i+k] + k
        #         j = i+k
        # i = j
        # jumps += 1

        jumps += 1

        i_greedy = [i+1, i+1]  # 0: next index to pick, 1: max index to reach
        for k in range(1, nums[i]+1):
            n1 = i+k  # next index
            n2 = n1 + nums[n1]  # max index to reach
            if n2 > i_greedy[1]:
                i_greedy = [n1, n2]

        i = i_greedy[0]

        # print(f'{i=} {jumps=}')

        if i >= n-1:
            break

    return jumps

nums = [2,3,1,1,4]
print(jumps(nums)) # expect 2

nums = [2,3,0,1,4]
print(jumps(nums)) # expect 2

nums = [3,3,1,2,4,1,1,1,1]
print(jumps(nums)) # expect 3
