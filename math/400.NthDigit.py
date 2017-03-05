"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""

# top solution 
# find the length of the number where the nth digit is from
# find the actual number where the nth digit is from
# find the nth digit and return
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        length = 1
        count = 9
        start = 1
        
        while n > length * count:
            n -= len*count
            length += 1
            count *= 10
            start *= 10
        
        start += (n-1) / length
        s = str(start)
        return int(s[(n-1)%length])
        
# top solution         
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        n -= 1
        for digits in range(1, 11):
            first = 10**(digits - 1)
            if n < 9 * first * digits:
                return int(str(first + n/digits)[n%digits])
            n -= 9 * first * digits