"""
Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
# hash 
class Solution(object):  # O(n) time, O(n) space
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        # import math
        # majority = math.floor(len(nums/2))
        majority = len(nums) // 2
        for x in nums:
            dic[x] = dic.get(x, 0) + 1
            if dic.get(x) >= majority:
                return x

                
# top solution: 
# Boyer–Moore majority vote algorithm
# O(n) time, O(1) space
# https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
# the algorithm finds a majority element, if there is one: that is, an element that occurs repeatedly for more than half of the elements of the input. However, if there is no majority, the algorithm will not detect that fact, and will still output one of the elements. A version of the algorithm that makes a second pass through the data can be used to verify that the element found in the first pass really is a majority.
class Solution(object):  
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:  # When count == 0 , it means nums[1...i ] doesn't have a majority, so nums[1...i ] will not help nums[1...n].And then we have a subproblem of nums[i+1...n].
                count += 1
                majority = nums[i]
            elif majority == nums[i]:
                count += 1
            else:
                count -= 1
        return majority
        
        
# top solution 
# sorting
# Since the majority element appears more than n / 2 times, the n / 2-th element in the sorted nums must be the majority element. 
class Solution(object):  
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()  # O(nlogn)
        return nums[len(nums)//2]
        
# pythonic
class Solution(object):  
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums)//2]

        
# top solution 
# Divide and Conquer
# The base case is that when the array has only one element, then it is the majority one.
class Solution(object):  
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def majority(nums, left, right):
            if left == right:
                return nums[left] # base case: when the array has only one element, then it is the majority one
            mid = left + ((right - left) >> 1)   # >> Bitwise right shift
            left_majority = majority(nums, left, mid)
            right_majority = majority(nums, mid + 1, right)
            if left_majority == right_majority:
                return left_majority
            return left_majority if nums[left: right+1].count(left_majority) > nums[left: right+1].count(right_majority) else right_majority
            
        return majority(nums, 0, len(nums)-1)    
        
# top solution 
# bit manipulation  
# get wrong answer when handling negative numbers
# The key lies in how to count the number of 1's on a specific bit. Specifically, you need a mask with a 1 on the i-the bit and 0 otherwise to get the i-th bit of each element in nums.       
class Solution(object):  
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = 0 
        n = len(nums)
        mask = 1
        for i in range(32):
            bit_count = 0
            for j in range(n):
                if nums[j] & mask:
                    bit_count += 1
                if bit_count > n//2:
                    majority |= mask
                    break
            mask <<= 1
        return majority