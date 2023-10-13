from typing import List


# Easy
def max_profit(self, prices: List[int]) -> int:
    max_profit = 0
    min_price = prices[0]
    for i in prices:
        if i < min_price:
            min_price = i
        else:
            diff = i - min_price
            max_profit = max(diff, max_profit)

    return max_profit
