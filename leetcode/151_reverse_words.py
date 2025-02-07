from functools import reduce
from operator import mul

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # answer = []
        # for i in range(len(nums)):
        #     answer.append(reduce(mul, nums[:i] + nums[i+1:]))
        # return answer

        answer = [1 for _ in range(len(nums))]

        left = 1
        for i in range(len(nums)):
            answer[i] *= left
            left *= nums[i]

        right = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer
