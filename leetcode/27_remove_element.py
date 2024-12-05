class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            # print(i, nums[i], k)
            if nums[i] == val:
                # if encounter val, then increment k to designate future shift
                k += 1
                # print(f'incremented {k=}')
            elif k > 0:
                # shift element k positions to left
                nums[i-k] = nums[i]
                # print(f'wrote {nums[i]=} into {nums[i-k]=}, {nums=}')
        return len(nums) - k
