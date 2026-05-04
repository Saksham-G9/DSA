from typing import List


def maxProfit(prices: List[int]) -> int:

    max_profit = 0

    curr_min = prices[0]

    for price in prices:

        if price < curr_min:
            curr_min = price
            continue

        curr_profit = price - curr_min

        max_profit = max(curr_profit, max_profit)
    
    return max_profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))
