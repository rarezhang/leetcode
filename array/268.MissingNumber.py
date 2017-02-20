""""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = [0 for _ in range(len(nums)+1)]
        for x in nums:
            temp[x] = 1
        for i in temp:
            if i == 0:
                return temp.index(i)
                
                
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #return sum(range(len(nums)+1)) - sum(nums)
        n = len(nums)  # modify according to the best solution
        return n*(n+1)/2 - sum(nums)
        
        
# top solution 
# bit manipulation: a^b^b=a
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = len(nums)  # the maximum number 
        for i in range(len(nums)):
            result = result ^ i ^ nums[i]
        return result 
        
        
# top solution 
# binary search 
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()  # inplace O(nlogn)
        left, right = 0, len(nums)
        while left < right:
            mid = (left+right)//2
            if nums[mid]>mid:
                right = mid 
            else:  # nums[mid]<=mid
                left = mid + 1
        return left