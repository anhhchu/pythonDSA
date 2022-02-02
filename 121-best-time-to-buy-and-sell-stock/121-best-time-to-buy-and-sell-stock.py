class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        maxright = 6
        maxprofit = max(6-7, 5) = 5
        
        7   1   5   3   6   4
        6   6   6   6   4   0
        
        """
        maxRight = 0
        maxProfit = 0
        for i in range(len(prices)-1, -1, -1):
            maxProfit = max(maxProfit, maxRight - prices[i])
            maxRight =  max(maxRight, prices[i])
            
        return maxProfit