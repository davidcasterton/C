class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # s = [] # subarray
        sm = sum(nums[:k]) # subarray max
        m = sum(nums[:k]) / k
        for i in range(k, len(nums)):
            sm += nums[i] - nums[i-k]
            if sm/k > m:
                m = sm/k
                # print(f'new max: {m=} {nums[i-k:i]=}')
        return m
