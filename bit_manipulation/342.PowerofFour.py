"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
"""
# top solution 

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Any number passes "n^(n-1)==0" must be powers of 2.
        # further categorized to 2 class:
        # (1) all numbers that are 2^(2k+1) 
        # (2) all numbers that 2^(2k) --> power of 4
        return num > 0 and num&(num-1)==0 and (num-1)%3==0
        
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Any number passes "n^(n-1)==0" must be powers of 2.
        # For power of 4, the additional restriction is that in binary form, the only "1" should always located at the odd position. For example, 4^0 = 1, 4^1 = 100, 4^2 = 10000. So we can use "num & 0x55555555==num" to check if "1" is located at the odd position.
        # 0x55555555  --> hex 
        # 0x55555555 == 0b1010101010101010101010101010101
        return num > 0 and num&(num-1)==0 and (num & 0x55555555) == num
            
s = Solution()
r = s.isPowerOfFour(16)
print(r)