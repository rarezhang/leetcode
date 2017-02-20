"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""


'''
# top solution
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 0  # anynumb xor 0 wil be the original number
        for x in nums:
            n ^= x  # ^ --> xor 
        return n
'''

# top solution: no extra memory
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]


# pythonic  
from functools import reduce   # python3     
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x,y: x^y, nums)
        
        
so = Solution()
r = so.singleNumber([1,1,2,3,3])    
print(r)


# other solution:  not space O(1)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for x in nums:
            dic[x] = dic.get(x, 0) + 1
        for x in nums:
            if dic[x] == 1:
                return x

                
                
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2*sum(set(nums)) - sum(nums)