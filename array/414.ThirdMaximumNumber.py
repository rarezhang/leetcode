"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""

# top solution
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_1, max_2, max_3 = None, None, None
        for x in nums:
            if x == max_1 or x == max_2 or x == max_3:
                continue
            if max_1 == None or x > max_1:
                max_3 = max_2
                max_2 = max_1
                max_1 = x
            elif max_2 == None or x > max_2:
                max_3 = max_2
                max_2 = x
            elif max_3 == None or x > max_3:
                max_3 = x
        return max_3 if max_3!=None else max_1
        
s = Solution()
r = s.thirdMax([3, 2, 1])    
print(r)


# top solution
class Solution(object):   # max is O(n)
    def thirdMax(self, nums):
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)
        

# pythonic 
class Solution(object):
    def thirdMax(self, nums):
        l = []
        for n in set(nums):
            bisect.insort(l, -n)
            del l[3:]
        return -l[2] if len(l)>2 else -l[0]  # max_3 exist