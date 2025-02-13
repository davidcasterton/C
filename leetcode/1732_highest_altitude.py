class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        elevation = [0]
        max_elevation = 0
        for i in range(len(gain)):
            e = elevation[i] + gain[i]
            elevation.append(e)
            if e > max_elevation:
                max_elevation = e
        return max_elevation
