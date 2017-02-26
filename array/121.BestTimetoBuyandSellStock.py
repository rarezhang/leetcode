"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """        
        max_difference = 0
        if not prices:
            return max_difference
            
        min_value = prices[0]
        for x in prices[1:]:
            if x < min_value:
                min_value = x
            if x - min_value > max_difference:
                max_difference = x - min_value                
        return max_difference

s = Solution()
r = s.maxProfit([])        
print(r)

# improvement
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """        
        max_difference = 0
        if not prices:
            return max_difference
            
        min_value = prices[0]
        for x in prices[1:]:
            min_value = min(x, min_value)
            max_difference = max(x - min_value, max_difference)
        return max_difference



# top solution
# Maximum subarray problem
# https://en.wikipedia.org/wiki/Maximum_subarray_problem
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """  
        max_current, max_sofar = 0, 0
        for i in range(1, len(prices)):
            max_current = max(0, max_current + prices[i] - prices[i-1])
            max_sofar = max(max_current, max_sofar)
        return max_sofar