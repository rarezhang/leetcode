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
        for n in nums:  # only need to handle number
            if n != 0:
                nums[insert_pos] = n
                insert_pos += 1
        while insert_pos < length:
            nums[insert_pos] = 0
            insert_pos += 1
        print(nums)
            

                    
s = Solution()
s.moveZeroes([0, 1, 0, 3, 12])