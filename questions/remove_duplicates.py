import math
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        print("input: ", nums, ", len: ", len(nums))
        for j in range(len(nums)):
            # print(j, nums[j])
            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i += 1
        # nums = list(set(nums))
        print("output: ", nums[:i], ", len: ", i)
        return i

sol = Solution()
print(sol.removeDuplicates([1,2,3,4,5]))
print(sol.removeDuplicates([1,2,2,3,4,5]))
print(sol.removeDuplicates([5,4,3,2,1]))
print(sol.removeDuplicates([5,4,3,2,2,1]))