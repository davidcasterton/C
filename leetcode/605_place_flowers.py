class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        _n = 0

        # special case edges
        if sum(flowerbed[:2]) == 0:
            _n += 1
            flowerbed[0] = 1
        if sum(flowerbed[-2:]) == 0:
            _n += 1
            flowerbed[-1] = 1

        for i in range(1, len(flowerbed)):
            if sum(flowerbed[i-1:i+2]) == 0:
                _n += 1
                flowerbed[i] = 1

        if _n >= n:
            out = True
        else:
            out = False
        return out
