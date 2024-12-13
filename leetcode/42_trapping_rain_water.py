class Solution:

    def trap(self, height: List[int]) -> int:

        # water = [0] * len(height)

        # left_max = 0
        # right_max = max(height[1:], default=0)

        # for i in range(1, len(height)):
        #     # find water height
        #     left_max = max(left_max, height[i-1])
        #     if height[i] == right_max:
        #         # calculate new right max
        #         right_max = max(height[i+1:]) if i+1<len(height) else 0
        #     water_height = min(left_max, right_max)

        #     # print(f'{i=} ({left_max} {right_max}) height: {water_height}')

        #     if water_height > 0:
        #         # find left peak
        #         for left_peak in range(i, -1, -1):
        #             if height[left_peak]>=water_height:
        #                 break
        #         # find right peak
        #         for right_peak in range(i, len(height)):
        #             if height[right_peak]>=water_height:
        #                 break

        #         # left_peak = max([index for index,value in enumerate(height[:i]) if value>=water_height])
        #         # right_peak = min([index+i for index,value in enumerate(height[i:]) if value>=water_height])

        #         # print(f' - {left_peak} {right_peak}')

        #         # calculate water at each index
        #         for k in range(left_peak, right_peak+1):
        #             water[k] = max(water[k], water_height-height[k])
        #             # print(f'   - {k} {water[k]}')

        #         # move i to right peak
        #         i = right_peak

        # # print(f'{water=}')
        # return sum(water)

        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]

        return water
