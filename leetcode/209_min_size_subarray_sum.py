class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        nums.sort(reverse=True)

        out: int = 0
        _sum: int = 0
        for i in range(len(nums)):
            _sum += nums[i]

            print(f'{i} {nums[i]=} {_sum=}')

            if _sum >= target:
                out = i+1
                break

        return out
