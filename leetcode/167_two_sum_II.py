class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # # O(n2)
        # for i in range(len(numbers)):
        #     for k in range(i+1, len(numbers)):
        #         if numbers[i] + numbers[k] == target:
        #             return [i+1, k+1]

        # O(n2) dual pointer
        for l in range(len(numbers)):
            if target > 0 and numbers[l] > target:
                continue  # skip, larger than target
            if l > 0 and numbers[l] == numbers[l-1]:
                continue  # skip, same as prior
            for r in range(len(numbers)-1, l-1, -1):
                if numbers[l] + numbers[r] == target:
                    return [l+1, r+1]
