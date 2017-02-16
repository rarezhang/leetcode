"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


# top solution
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length < 2:
            return 
        insert_pos = 0    
        for n in nums:  # only handle number not equal to 0 
            if n != 0:
                nums[insert_pos] = n
                insert_pos += 1
        while insert_pos < length:  # add enough 0s
            nums[insert_pos] = 0
            insert_pos += 1
        print(nums)
            

                    


# top solution
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0  # position of first num not equal to 0
        
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1    
            i += 1
        print(nums)
        


# pythonic 
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
        nums.sort(key=lambda x:1 if x==0 else 0)
        # For non-0, lambda function will return False which would turn into 0 and for 0 lambda will return True which will turn into 1. Therefore, 0 value will follow non-0 value
        print(nums)
        
s = Solution()
s.moveZeroes([0, 1, 0, 3, 12])        