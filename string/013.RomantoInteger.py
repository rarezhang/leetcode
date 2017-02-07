"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

"""

# The system for writing Roman Numerals is an additive system. This means to calculate the value of a Roman Numeral, you simply have to add up all the digits in the Roman Numeral!


# You can write a smaller numerals to the left of a larger one to subtract from it


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = 0
        post_cha = "I"
        for cha in reversed(s):
            if dic[cha] >= dic[post_cha]:
                result += dic[cha]
            else:
                result -= dic[cha]
            post_cha = cha
        return result 
        
        
# pythonic 
dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, p = 0, 'I'
        for c in s[::-1]:
            res, p = res - dic[c] if dic[c] < dic[p] else res + dic[c], c
        return res
        