class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0  # max profit

        min_i = prices.index(min(prices))
        max_i = prices.index(max(prices))
        if min_i < max_i:
            # special case where can immediately compute max profit
            p = prices[max_i] - prices[min_i]
            # print(f'special case: {min_i=} {max_i=} {p=}')
        elif len(prices) >= 2:
            # full solution

            b = 0 # buy day
            s = 1 # sell day
            p = prices[s] - prices[b]  # max profit of current sublist
            for i in range(1, len(prices)):
                if prices[i] < prices[b]:
                    # move buy day & sell day
                    b = i
                    s = i

                if prices[i] - prices[b] > prices[s] - prices[b]:
                    # move sell day
                    s = i

                p = max(p, prices[s] - prices[b])
                # print(f'{i} {p=} {b=} {s=}')

        # return 0 if cannot achieve profit
        p = 0 if p < 0 else p

        return p
