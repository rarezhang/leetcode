"""
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""

class Solution(object):  # O(2n)
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for x in nums:  # O(n)
            dic[x] = dic.get(x, 0) + 1
        for x in nums:  # O(n)
            if dic.get(x) > 1:
                return True
        return False
        
# top solution: O(n) 
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for x in nums:  #O(n)
            if x in dic:
                return True
            else:
                dic[x] = 1
        return False

        
# top solution: O(nlogn)        
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()  # O(nlogn)
        for i in range(1, len(nums)):  # worst case: O(n)
            if nums[i] == nums[i-1]:
                return True
        return False
        
        
# pythonic 
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # set(list) -> O(n)
        return len(nums) == len(set(nums))