"""
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = bin(n)[2:]  # bin() return string, [2:] get rid of '0bxxx'
        count = 0
        for s in n:
            if s == '1':
                count += 1
        return count  

        
# pythonic 
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')
        
s = Solution()
r = s.hammingWeight(11)
print(r)


# top solution: bit shifting 
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 0:
            # if n&1==1: the last bit of n is 1 
            count += n&1
            n = n >> 1  # right shift: Returns n with the bits shifted to the right by 1 places. This is the same as //'ing n by 2**1. 
        return count

# top solution 
# Each time of "n &= n - 1", we delete one '1' from n.        
# e.g., 7 -> 111 -> total 3
# 7&(7-1) -> 111&110 -> 11(3)
# 3&(3-1) -> 11&10 -> 1(1)
# 1&(1-0) -> 1&0 -> 0
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n = n&(n-1)
            count += 1
        return count 