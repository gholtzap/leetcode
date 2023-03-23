class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 'moving window' problem: we will keep two pointers, l:int and r:int
        # we will move r:int until it is greater than l:int
        #   we will then compute if the profit is greater than our 'high score'
        #      if it is, then we redefine our 'high score' and go on our business.
        #   else, we will iterate l:int to r:int and continue the process
        
        l,r = 0,1
        maxProfit = 0

        if(len(prices)==0): 
            return 0
        else:
            while r < len(prices):
                if(prices[l] < prices[r]):
                    profit = prices[r]-prices[l]
                    maxProfit = max(maxProfit, profit)
                else:
                    l=r
                r+=1

        return maxProfit