# Solution 1 
# O(n), O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        lowest = prices[0]
        for x in prices:
            if x<lowest:
                lowest = x
            profit = max(profit, x-lowest)

        return profit