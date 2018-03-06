"""
697. Degree of an Array

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2] -> [2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""



# top solution 
import collections

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # get the degree of nums 
        '''
        a_dict = dict()
        for n in nums:
            if n in a_dict:
                a_dict[n] += 1
            else:
                a_dict[n] = 1
        degree = max(a_dict.values())  
        '''
        c = collections.Counter(nums)
        degree = max(c.values())
        
        # first: first index of the value; last: last index of the value
        first, last = {}, {}
        for i, v in enumerate(nums):
            first.setdefault(v, i) # setdefault: if the key not in the dict, set the value; otherwise, skip 
            last[v] = i
        
        # the length of all subsets have the maximum degree
        len_subsets = [last[v] - first[v] + 1 for v in c if c[v] == degree]
        
        # smallest possible length of a subarray of nums
        return min(len_subsets)
        
        
        
        
        
        
        
s = Solution()
nums = [1, 2, 2, 3, 1]
nums = [1,2,2,3,1,4,2]
r = s.findShortestSubArray(nums)
print(r)        
