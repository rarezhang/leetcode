"""
Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
"""

'''
# find median point, statistics in python 3.4 
from statistics import median
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = median(nums)
        result = 0
        for x in nums:
            result += abs(x-m)
        return result
        

# similar to "meeting point" problem
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()  # O(n*logn)
        i,j = 0,len(nums)-1
        count = 0
        while i < j:  # O(n)
            count += nums[j] - nums[i]
            i += 1
            j -= 1
        return count 


# quick select, find median
# https://en.wikipedia.org/wiki/Quickselect
# when nums is a long list, RecursionError: maximum recursion depth exceeded in comparison
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        def select_kth(k, nums, start, end):
            # pivot is the kth smallest element 
            pivot = nums[end]  # start with random pivot, here must start with end 
            left, right = start, end
            while True:
                while (left < right) and (nums[left] < pivot):
                    left += 1
                while (left < right) and (nums[right] >= pivot):
                    right -= 1
                if left == right:
                    break
                nums[left], nums[right] = nums[right], nums[left]  # swap 
            nums[left], nums[end] = nums[end], nums[left]  # swap 
            if k == left+1:
                return pivot
            elif k < left+1:
                return select_kth(k, nums, start, left-1)
            else: # k > left
                return select_kth(k, nums, left+1, end)
            
                
        def find_median(nums):
             return select_kth(len(nums)//2+1, nums, 0, len(nums)-1)
            
        """
        def find_median(nums):
            if len(nums)%2:  # odd length 
                return select_kth(len(nums)//2, nums, 0, len(nums)-1)
            else:  # even length
                left = select_kth((len(nums)-1)//2, nums, 0, len(nums)-1)
                right = select_kth((len(nums)+1)//2, nums)
                return (left+right)/2
        """
        
        result = 0
        median = find_median(nums)
        for x in nums:
            result += abs(median-x)
        return result
'''           
            

# pythonic 

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        median = sorted(nums)[len(nums)//2]
        return sum([abs(n-median) for n in nums])



class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum([nums[~i]-nums[i] for i in range(len(nums)//2)])

# ~ operator: 
# operator.inv(obj)
# operator.invert(obj)
# operator.__inv__(obj)
# operator.__invert__(obj)
# Return the ```bitwise inverse of the number obj```. This is equivalent to ~obj.
# 0, 1, 2, ... get turned into -1, -2, -3, ...
# nums[~i] - nums[i] if i = 0
# nums[-1] - nums[0]
        
        
s = Solution()
num = [1,2,4]
c = s.minMoves2(num)
print(c)
