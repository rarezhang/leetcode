"""
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].
"""

# time limit exceeded 
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = []
        nums.sort()
        while len(nums) > 0:
            x = nums.pop()            
            if (x - k) in nums:
                result.append((x, x-k))
        return len(set(result))         

        
# top solution: hash map         
class Solution(object): # O(2n) -> O(n)
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0 or k < 0:
            return 0
        dic = {}        
        for x in nums:  # O(n)
            dic[x] = dic.get(x, 0) + 1
        # result = 0 
        if k == 0: # O(n)
            result = sum([1 for x in dic if dic[x] >= 2])
            # for x in dic:
                # if dic[x] >= 2:
                    # result += 1
        else: # O(n)
            result = sum([1 for x in dic if x+k in dic])
            # for x in dic:
                # if x+k in dic:
                    # result += 1
        return result
                
        
        
        
# top solution 
# two pointers         
class Solution(object):  # O(n + n*log(n)) --> O(n*log(n))
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()  # O(n*log(n))
        result = 0
        i, j = 0, 1
        while j < len(nums):  # O(n)
            # have to put this condition first 
            # since control j in the loop 
            if (j <= i) or (nums[j] - nums[i] < k):
                j += 1
            # i > 0 and nums[i] == nums[i-1] --> identical numbers 
            elif (i > 0 and nums[i] == nums[i-1]) or (nums[j] - nums[i] > k):
                i += 1
            else:  # nums[j] - nums[i] == k:
                i += 1
                result += 1
        return result  

        
# pythonic 
import collections
class Solution(object):  
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k > 0:
            return len(set(nums) & set(n+k for n in nums))
        elif k == 0:
            return sum(v>1 for v in collections.Counter(nums).values())
        else:
            return 0
            
# pythonic 
# import collections
class Solution(object):  
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return len(set(nums)&{n+k for n in nums}) if k>0 else sum(v>1 for v in collections.Counter(nums).values()) if k==0 else 0
        
        
sol = Solution()

alist = [3, 1, 4, 1, 5]
k = 2  # result = 2

alist = [1,1,1,1,1]
k = 0  # result = 1

# alist = [6,7,3,6,4,6,3,5,6,9]
# k = 4  # result = 2

# alist = [1,2,3,4,5]
# k = 3
print(sol.findPairs(alist, k))        