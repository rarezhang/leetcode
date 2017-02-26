"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""


        
        
# top solution 
# dynamic programming 
# figure out: the format of the sub problem (or the state of each sub problem) -> come up with the recursive relation.
# O(n) space, O(n) time
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        dp = [x for x in nums]
        dp[0] = max_sum = nums[0]
        
        for i in range(1, length):
            if dp[i-1] > 0:
                dp[i] = nums[i] + dp[i-1]
            max_sum = max(max_sum, dp[i])
        return max_sum
        
# improvement
# do not need to record every dp[i]
# O(1) space O(n) time
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        cur_sum = max_sum = nums[0]
        for i in range(1, length):
            if cur_sum > 0:
                cur_sum = nums[i] + cur_sum
            else:
                cur_sum = nums[i]
            max_sum = max(cur_sum, max_sum)
        return max_sum
        
        
# top solution 
# this problem was discussed by Jon Bentley (Sep. 1984 Vol. 27 No. 9 Communications of the ACM P885)
'''
copied from this paper 

algorithm that operates on arrays: it starts at the left end (element A[1]) and scans through to the right end (element A[n]), keeping track of the maximum sum subvector seen so far. The maximum is initially A[0]. Suppose we've solved the problem for A[1 .. i - 1]; how can we extend that to A[1 .. i]? The maximum
sum in the first I elements is either the maximum sum in the first i - 1 elements (which we'll call MaxSoFar), or it is that of a subvector that ends in position i (which we'll call MaxEndingHere).

MaxEndingHere is either A[i] plus the previous MaxEndingHere, or just A[i], whichever is larger.
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        current_sum = max_sum = nums[0]
        for x in nums[1:]:
            current_sum = max(x, current_sum+x)
            max_sum = max(max_sum, current_sum)
        return max_sum