"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
"""
# top solution
# a square number is 1+3+5+7+... Time Complexity O(sqrt(N))
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1: return False
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0
        
# top solution 
# binary search, time complexity O(logN)
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1: return False
        
        left, right = 1, num
        while left <= right:
            mid = left + (right - left) / 2
            if mid * mid > num:
                right = mid - 1
            elif mid * mid < num:
                left = mid + 1
            else:
                return True 
        return False

# top solution         
# newton's method: updating rule: result = (result + x/result) / 2
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        r = num
        while r * r > num:
            r = (r + x/r) / 2
        return r * r == x
        

        
s = Solution()
print(s.isPerfectSquare(14))
        