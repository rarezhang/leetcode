"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
"""


# important:  use (n-1)%26 instead, then we get a number range from 0 to 25.
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = []
        while n != 0:
            n, cha = divmod(n-1,26)
            result.append(chr(cha+ord('A')))
        return ''.join(reversed(result))
        
s = Solution()
num = 26
r=s.convertToTitle(num)
print(r)


# pythonic 
# recursion
class Solution(object):
    def convertToTitle(self, num):
        """
        :type n: int
        :rtype: str
        """
        return "" if num == 0 else self.convertToTitle((num - 1) / 26) + chr((num - 1) % 26 + ord('A'))