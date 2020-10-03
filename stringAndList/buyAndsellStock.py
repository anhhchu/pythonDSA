'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        O(N) only iterate through the list once, O(1) space with profit and maxVal as local variables
        """
        
        if len(prices) < 2:
            return 0
        elif len(prices) == 2:
            return max(0, prices[1] - prices[0])
        
        # iterate from right to left prices[-2],0
        # compare difference between profit and difference between a value and the max val to its right
        profit = 0
        maxVal = prices[-1]
        for i in range(len(prices)-2,-1,-1):
            val = prices[i]
            if maxVal > val:
                profit = max(profit, maxVal-val)
            else:
                maxVal = val
                
        return profit