"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

# top solution 
# just count the number of same pairs, then this can be used to put in the different direction to consist of palindrome. Then if there exist more chars, we can put one in the middle.
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = set()
        for x in s:
            if x in dic:  # O(1)
                dic.remove(x)
            else:
                dic.add(x)
        odd = len(dic)
        return len(s) if odd == 0 else len(s) - (odd - 1)



        
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        odds = 0
        for x in s:
            dic[x] = dic.get(x, 0) + 1
        for k in dic:
            if dic[k] % 2 == 1:
                odds += 1
        return len(s) if odds == 0 else len(s) - (odds - 1)
                

# pythonic 
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odds = sum(v & 1 for v in collections.Counter(s).values())
        return len(s) - odds + bool(odds)
        """
        1 & 1 = 1
        2 & 1 = 0
        3 & 1 = 1
        ..
        ..
        """
        