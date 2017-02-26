"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

# top solution 
# "a <= b <= c <= d", the profit is "d - a = (b - a) + (c - b) + (d - c)" 
# "a <= b >= b' <= c <= d", profit is "(b - a) + (d - b')"
# target at monotone sequences.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                total += prices[i] - prices[i-1]
        return total        

        
# pythonic         
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum([max(prices[i] - prices[i-1], 0) for i in range(1, len(prices))])
        