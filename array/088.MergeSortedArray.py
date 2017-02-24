"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
"""

# top solution 
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:  # once all of the numbers from nums2 have been merged into nums1, the rest of the numbers in nums1 that were not moved are already in the correct place.
            nums1[:n] = nums2[:n]
            
            
# top solution 
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while n > 0:
            # nums2 has larger end 
            if m <=0 or nums2[n-1] >= nums1[m-1]:  # m<0: nums1 already end 
                nums1[m+n-1] = nums2[n-1]
                n -= 1 
            else: # nums1 has larger end 
                nums1[m+n-1] = nums1[m-1]
                m -= 1