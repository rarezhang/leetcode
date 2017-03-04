"""
Given an integer, write a function to determine if it is a power of two.
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        if n == 1:
            return True
        while n > 1:
            if n % 2 != 0:
                return False
            n //= 2
        return True
        
# top solution: iterative
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1
        
# top solution: recursive 
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True 
        elif n > 0 and n%2==0:
            return self.isPowerOfTwo(n//2)
        else:
            return False
            
# improvement            
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n==1 or (n%2==0 and self.isPowerOfTwo(n//2)))
        
# top solution: bit manipulation 
# Power of 2 means only one bit of n is 1
# use the trick n&(n-1)==0 to judge whether that is the case
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return n&(n-1)==0
        
# top solution 
# improvement 
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n > 0) and (n&(n-1)==0)

# top solution: Math derivation
# Because the range of an integer = -2147483648 (-2^31) ~ 2147483647 (2^31-1), the max possible power of two = 2^30 = 1073741824. 
# (1) If n is the power of two, let n = 2^k, where k is an integer.
# We have 2^30 = (2^k) * 2^(30-k), which means (2^30 % 2^k) == 0.
# (2) If n is not the power of two, let n = j*(2^k), where k is an integer and j is an odd number.
# We have (2^30 % j*(2^k)) == (2^(30-k) % j) != 0.

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (1073741824 % n == 0)  # O(n)