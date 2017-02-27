"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
"""

# top solution  
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == 0:
            return b
        if b == 0:
            return a
            
        while b != 0:
            carry = a & b  # get different bits
            a = a ^ b  # gets double 1s
            b = carry << 1  # << moves carry
        return a

        
# top solution  
# maximum recursion depth exceeded 
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return a if b==0 else self.getSum(a^b, (a&b)<<1)    