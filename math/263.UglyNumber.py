"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
"""

# top solution 
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num > 0:
            for p in 2, 3, 5:  # if there are lots of loarge numbers: 30,15,10,9,8,6,5,4,3,2
                while num % p == 0:
                    num /= p
        return num == 1
        