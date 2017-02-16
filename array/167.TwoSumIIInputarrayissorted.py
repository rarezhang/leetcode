"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

# exceed time limit 
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        while i < len(numbers):
            y = target - numbers[i]
            j = i+1
            while j < len(numbers) and numbers[j] <= y:                
                if numbers[j] == y:
                    return i+1, j+1
                j += 1
            i += 1    

            
# top solution: two pointers 
#  A points to index 0, B points to index len - 1, shrink the scope based on the value and target comparison.
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """           
        left, right = 0, len(numbers)-1
        while left < right:
            value = numbers[left] + numbers[right]
            if value == target:
                return left+1, right+1
            elif value > target:
                right -= 1
            else:  # value < target:
                left += 1
        return []        

# dictionary 
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        dic = {}
        for i, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i
        
# binary search
class Solution(object):        
    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            left, right = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while left <= right:
                mid = left + (right-left)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    left = mid+1
                else:
                    right = mid-1

            
s = Solution()
numbers = [5,25,75]
r = s.twoSum(numbers, 100)
print(r)
        