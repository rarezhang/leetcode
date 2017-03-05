"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
"""

# top solution 
# recursive 
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n==1 or (n%3==0 and self.isPowerOfThree(n/3)))
        
# top solution 
# iterative         
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 1:
            while n%3 == 0:
                n /= 3
        return n == 1
        
# top solution 
# Find the maximum integer that is a power of 3 and check if it is a multiple of the given input.
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        maxPowerOfThree = 1162261467
        return n > 0 and maxPowerOfThree % n == 0

# top solution 
# hash set         
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set(1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467)
        return True if n in s else False
        
