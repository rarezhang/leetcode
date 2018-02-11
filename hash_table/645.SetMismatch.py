"""
645. Set Mismatch

The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.

# hash table; math

"""

class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                result.append(nums[i])
        origin_sum = sum(nums)
        N = len(nums)
        assume_sum = N* (1+N)/2
        result.append(int((assume_sum - origin_sum) + result[0]))
        return result


# top solution 
class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        count_list = [0] * (N+1)  # nums: 1...N
        for n in nums:
            count_list[n] += 1
        for c in range(1, N+1):
            if count_list[c] == 0:
                never = c
            if count_list[c] == 2:
                twice = c
        return [twice, never]        


class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        N = len(nums)
        # for each number we found, set nums[num-1] to its negative value
        for i in range(N):
            # index starts from 0, and the set starts from 1
            idx = abs(nums[i])-1
            if nums[idx] > 0: 
                nums[idx] = -nums[idx]
            else: # found the duplicate number
                result.append(idx + 1)
        # only nums[missing number -1] > 0
        for j in range(N):
            if nums[j] < 0:
                nums[j] = -nums[j]  # restore the original values
            else:
                result.append(j+1)  # since index starts from 0, and the set starts from 1
        return result        


            
s = Solution()
a_list = [1,2,2,4]
r = s.findErrorNums(a_list)
print(r)
if r == [2,3]:
    print('pass')
else:
    print('error')
        

