class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        out = False
        i = nums[0]
        k = nums[-1]

        for j in range(1,len(nums)-1):
            if nums[j-1] < nums[i]:
                i = j-1

            valid_i = False
            if nums[i] < nums[j]:
                valid_i = True
            if not valid_i:
                continue

            valid_k = False
            right_max = max(nums[j+1:])
            if right_max > nums[j]:
                valid_k = True

            if valid_i and valid_k:
                out = True
                break
            else:
                # only continue if smaller j available to right
                right_min = min(nums[j+1:])
                if right_min >= nums[j]:
                    break

        return out
