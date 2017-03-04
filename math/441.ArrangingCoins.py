"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
"""

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        row = 1
        while True:
            if row*(row+1) > 2*n:
                return row - 1
            else:
                row += 1
                
# top solution O(1)
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + ... + x <= n
# (x * ( x + 1)) / 2 <= n`
# a = 1, b = 1, c = -2*n
# x = (-1 + sqrt(1 - 4*1*(-2*n))) / 2
# simplify: x = (-1 + sqrt(1 + 8.0*n)) / 2               
import math
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((-1 + math.sqrt(1 + 8*n)) // 2) 
        
# top solution 
# binary search O(logn)
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end= 0, n
        while start <= end:
            mid = start + (end - start) // 2
            if mid * (mid + 1) <= 2* n:
                start = mid + 1
            else:
                end = mid - 1
        return int(start - 1)