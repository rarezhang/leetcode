"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        d = len(digits) - 1
        n = 0
        for x in digits:
            n += x*10**d
            d -= 1
        n += 1
        return [int(st) for st in str(n)]
            
s = Solution()
r = s.plusOne([9,9,9])    
print(r)    


# top solution 
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        d = len(digits)
        i = d - 1
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                return digits            
            digits[i] = 0  # if digits[i] == 9
            i -= 1
        # The last part of code is only for the case that the whole input array is 9s.
        # For example : 99999-----> 100000
        # Any other case would return in the loop.
        new_digits = [0 for _ in range(d+1)]
        new_digits[0] = 1
        return new_digits
        
            
s = Solution()
r = s.plusOne([1,9,9])    
print(r)  


# top solution 
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        i = n - 1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
            i -= 1
            
        new_digits = [0 for _ in range(n+1)]
        new_digits[0] = 1
        return new_digits
        
        
# pythonic 
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = reduce(lambda x,y:x*10+y,digits)+1
        return [int(i) for i in str(digits)]