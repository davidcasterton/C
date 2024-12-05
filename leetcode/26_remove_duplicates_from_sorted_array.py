class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        k = 1  # num unique elements
        for i in range(1, len(nums)):
            if nums[i] not in nums[0:k]:
                nums[k] = nums[i]
                k += 1

        return k
