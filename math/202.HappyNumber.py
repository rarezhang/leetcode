"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def digits(n):
            d = []
            while n != 0:
                d.append(n%10)
                n //= 10
            return d
        
        def new_n(n):
            d = digits(n)
            nn = 0
            for x in d:
                nn += x**2 
            return nn
        
        if n < 0: return False
        numbers = set()  # set is better than list
        while True:
            if n == 1:
                return True 
            if n in numbers: # O(1)
                return False
            numbers.add(n)
            n = new_n(n)
            
s = Solution()
r = s.isHappy(22)
print(r)


# top solution 
# Floyd Cycle detection algorithm
#  the algorithmic problem of finding a cycle in a sequence of iterated function values

# starting from a number I, if some value - say a - appears again during the process after k steps, the initial number I cannot be a happy number.

# a non-happy number will definitely generate a loop: for any non-happy number, all outcomes during the process are bounded by some large but finite integer N.
# If all outcomes can only be in a finite set (2,N], and since there are infinitely many outcomes for a non-happy number, there has to be at least one duplicate, meaning a loop!

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """       
        def new_n(n):
            nn, temp = 0, 0
            while n != 0:
                temp = n % 10
                nn += x**2
                n //= 10
            return nn
        slow = fast = n
        while True:
            slow = new_n(slow)
            fast = new_n(fast = new_n(fast))            
            if fast == 1: return True
            if slow == fast:
                break 
        return True 
        
            
        
            
               