class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)

        # left to right
        for i in range(len(ratings)):
            greater_rating_than_left = True if (i-1>=0 and ratings[i] > ratings[i-1]) else False
            if greater_rating_than_left:
                candies[i] = candies[i-1] + 1

        # right to left
        for i in range(len(ratings)-1, -1, -1):
            greater_rating_than_right = True if (i+1<len(ratings) and ratings[i] > ratings[i+1]) else False
            less_candy_than_right = True if (i+1<len(ratings) and candies[i] <= candies[i+1]) else False
            if greater_rating_than_right and less_candy_than_right:
                candies[i] = max(candies[i+1] + 1, candies[i] + 1)
            # print(f'{greater_rating_than_right} {less_candy_than_right}')

        # print(candies)
        return sum(candies)
