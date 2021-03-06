"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""

# top solution
# when find a number i, flip the number at position i-1 to negative. 
# if the number at position i-1 is already negative, i is the number that occurs twice.
    

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        for i in range(len(nums)):
        
            index = abs(nums[i])-1
            if nums[index] < 0:
                result.append(index+1)
            nums[index] = -nums[index]
        return result
            
s = Solution()   
r = s.findDuplicates([4,3,2,7,8,2,3,1])
print(r)      