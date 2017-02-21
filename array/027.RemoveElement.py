"""
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.

"""
# top solutuion 
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        '''
        new_tail = 0
        i = 0
        while i < len(nums):
            if nums[i] != val:                
                nums[new_tail] = nums[i]
                new_tail += 1
            i += 1
        return new_tail
        '''
        new_tail = 0
        for x in nums:
            if x != val:
                nums[new_tail] = x 
                new_tail += 1
        return new_tail

        
        
# top solution
"""
scans numbers from the left to the right, one by one.

Once it finds a number that equals to elem, swaps current element with the last element in the array and then dispose the last.

The swapping can be optimized as overwrite current element by the last one and dispose the last.
Now, we have removed the current number, and the length of the array is reduced by 1.

To ensure we do not make wrong choices, we will continue scanning from the (new) current element.
So it won't fail if the same number is swapped to the current position.
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left, right = 0, len(nums)
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right-1]
                right -= 1
            else:
                left += 1
        return right
        
