class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        r = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= m:
                r.append(True)
            else:
                r.append(False)
        return r
