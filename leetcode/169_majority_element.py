class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_element = nums[0]
        elements = {majority_element: 1}

        for num in nums[1:]:
            try:
                elements[num] += 1
            except KeyError:
                elements[num] = 1
            if elements[num] > elements[majority_element]:
                majority_element = num

        return majority_element
