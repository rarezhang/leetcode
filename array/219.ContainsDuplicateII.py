"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
"""

# Time Limit Exceeded
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j] and j - i <= k:
                    return True
                j += 1
            i += 1
        return False 

        
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for j, x in enumerate(nums):
            if x in dic:
                i = dic[x]
                if j - i <= k:
                    return True
            dic[x] = j
        return False
        
# pythonic: better than above  
# dict.get(key) returns None if the key doesn't exist, and somenumber <= None always returns False. So I don't have to first check whether the number has occurred before and then check whether it has occurred recently.
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        index = {}
        for i, x in enumerate(nums):
            if i - k <= index.get(x)
                return True
            index[x] = i
        return False
        
dict.get(key) returns None if the key doesn't exist, and somenumber <= None always returns False. So I don't have to first check whether the number has occurred before and then check whether it has occurred recently.

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        index = {}
        for i, n in enumerate(nums):
            if i - k <= index.get(n):
                return True
            index[n] = i
        return False

# top solution 
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        aset = set()
        # i current index 
        # aset include all elements whose index j - i <= k
        for i in range(len(nums)):
            if i > k:
                aset.remove(nums[i-k-1])
            if nums[i] in aset: # O(1)
                return True
            else:
                aset.add(nums[i])
        return False    