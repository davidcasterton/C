import copy


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = copy.deepcopy(nums)
        right = copy.deepcopy(nums)

        # sum from left
        for i in range(1, n):
            left[i] *= left[i-1]
        # print(f'{left=}')

        # sum from right
        for i in range(2, n+1):
            right[-i] *= right[-i+1]
        # print(f'{right=}')

        # shift left list to the right
        left.insert(0,1)
        left.pop(-1)

        # shift right list to the left
        right.pop(0)
        right.append(1)

        # print(f'{left=}  {right=}')

        res = [a*b for a, b in zip(left, right)]

        return res
