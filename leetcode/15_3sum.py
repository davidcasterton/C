
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # sort input list in place
        len_nums = len(nums)

        out: list[list[int, int, int]] = []  # output list of lists

        # # O(n3)
        # sl = list[int, int, int]  # sub-list
        # for i in range(len_nums):
        #     for j in range(i+1, len_nums):
        #         for k in range(j+1, len_nums):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 sl = sorted([nums[i], nums[j], nums[k]])
        #                 if sl not in out:
        #                     out.append(sl)

        # O(n2) 2 pointer
        for i in range(len_nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # skip, same as prior

            j: int = i+1
            k: int = len_nums-1
            _sum: int = -1


            while j < k:
                _sum = nums[i] + nums[j] + nums[k]
                if _sum == 0:
                    out.append([nums[i], nums[j], nums[k]])
                    j+= 1
                    while nums[j] == nums[j-1] and j<k:
                        j+=1
                elif _sum < 0:
                    # increase left pointer to larger number
                    j += 1
                elif _sum > 0:
                    # decrease right pointer to smaller number
                    k -= 1

        return out
