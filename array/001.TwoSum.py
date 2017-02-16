"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        for i in range(len(nums)):
            j = dic.get(target - nums[i], -1)
            if j != -1 and i!=j:  # i!=j -> may not use the same element twice.
                return [i, j]
            
s = Solution()
r = s.twoSum([2, 7, 11, 15], 9)      
r = s.twoSum([3,2,4], 6)       
print(r)


# top solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i,num in enumerate(nums):
            if target-num in dic:
                return dic[target-num], i
            d[num]=i