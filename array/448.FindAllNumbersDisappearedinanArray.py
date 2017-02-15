"""
Given an array of integers where 1 = a[i] = n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

# top solution
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        
        for i in range(len(nums)):
            value = abs(nums[i]) - 1 
            if nums[value] > 0:  # if already handled, won't do it again
                nums[value] = -nums[value]  # put that value at appropriate index 
                
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        return result
        
        
# top solution
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        
        length = len(nums)
        for i in range(length):
            nums[(nums[i]-1)%n] += n  # (nums[i]-1)%n the correct index for nums[i]
        for i in range(length):
            if nums[i] <= n:
                result.append(i+1)
        return result
        
        
# pythonic 
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [0] + nums
        for i in range(len(nums)):
            index = abs(nums[i])
            nums[index] = -abs(nums[index])
        
        return [i for i in range(len(nums)) if nums[i] > 0]