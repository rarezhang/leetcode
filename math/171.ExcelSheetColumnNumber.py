"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        def get_num(cha):
            return ord(cha)-ord('A')+1
        result, pos = 0, 0    
        for cha in reversed(list(s)):
            result += get_num(cha)*26**pos
            pos += 1
        return result 


# top solution 
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for cha in s:
            result *= 26
            result += ord(cha)-ord('A') + 1
        return result

        
# pythonic 
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return reduce(lambda x,y:x*26+y,map(lambda x:ord(x)-ord('A')+1,s))
# e.g.,
# BAA = 2*26**2 + 1*26**1 + 1*26**0 
# map(lambda x:ord(x)-ord('A')+1,s): BAA -> 211
# reduce(lambda x,y:x*26+y, [2,1,1]): (2*26+1)*26+1