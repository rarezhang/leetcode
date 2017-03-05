"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

trailing zeros are a sequence of 0 in the decimal representation (or more generally, in any positional representation) of a number, after which no other digits follow.

"""


# top solution 
# Because all trailing 0 is from factors 5 * 2.
# But sometimes one number may have several 5 factors, for example, 25 have two 5 factors, 125 have three 5 factors. In the n! operation, factors 2 is always ample. So we just count how many 5 factors in all number from 1 to n.
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n >= 5:
            n /= 5
            result += n 
        return result

        
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n == 0 else n / 5 + self.trailingZeroes(n/5)