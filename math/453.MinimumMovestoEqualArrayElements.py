"""
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.
"""

# top solution 
# Incrementing all but one is equivalent to decrementing that one. 
# How many single-element decrements to make all equal? 
# No point to decrementing below the current minimum, so how many single-element decrements to make all equal to the current minimum? 
# Just take the difference from what we currently have (the sum) to what we want (n times the minimum).

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)
        
# top solution:
# only care about the difference between elements instead of the final value. In the perspective of difference, add one to all the other elements is equivalent to subtract one from current element.
# Adding 1 to n - 1 elements is the same as subtracting 1 from one element, w.r.t goal of making the elements in the array equal.
# So, best way to do this is make all the elements in the array equal to the min element.        
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_value = nums[0]
        for x in nums[1:]:
            if x < min_value: min_value = x
        result = 0    
        for x in nums:
            result += x - min_value
        return result 
        