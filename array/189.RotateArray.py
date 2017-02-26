"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
"""


# top solution. space O(n)
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n   # more than one loop 
        nums[:] = nums[n-k:] + nums[:n-k]
        # must use nums[:] --> in place
        # nums = xxx --> return a new list 
        
#  improvement using negative index:
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

        
# top solution 
# Make an extra copy then rotate.
# Time complexity: O(n). Space complexity: O(n)
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length < 2 or k < 1:
            return 
            
        new_nums = [x for x in nums]  # make a copy of nums
        
        # rotate the elements 
        for i in range(length):
            nums[(i+k)%length] = new_nums[i]
            
