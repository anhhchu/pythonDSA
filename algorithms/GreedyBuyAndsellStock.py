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

#### OTHER SOLUTIONS

def get_max_profit_bad(stock_prices):
    '''
    O(N^2) time 
    '''
    # Calculate the max profit
    if len(stock_prices)<=1: 
        raise ValueError('require 2 prices')
        
    
    for i in range(len(stock_prices)-1):
        if i == 0:
            maxProfit = max(stock_prices[i+1:]) - stock_prices[i]
        currProfit = max(stock_prices[i+1:]) - stock_prices[i]
        maxProfit = max(currProfit, maxProfit)

    return maxProfit

def get_max_profit(stock_prices):
    '''
    better solution with O(n) time, O(1) space
    '''
    if len(stock_prices) <= 1:
        raise ValueError('require 2 prices')

    minPrice = stock_prices[0]
    maxProfit = stock_prices[1] - stock_prices[0]

    for i in range(1, len(stock_prices)):
        currProfit = stock_prices[i] - minPrice
        minPrice = min(minPrice, stock_prices[i])
        maxProfit = max(maxProfit, currProfit)

    return maxProfit

# Tests

import unittest

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])


unittest.main(verbosity=2)