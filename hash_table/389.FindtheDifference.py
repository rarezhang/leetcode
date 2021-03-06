"""
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
"""


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        for x in s:
            dic[x] = dic.get(x, 0) + 1
        for x in t:
            if x not in dic:
                return x
            else:
                dic[x] = dic.get(x) - 1
                if dic[x] == 0:
                    del dic[x]
        return dic.keys()[0]
                
                
# top solution 
# bit manipulation 
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        c = 0
        for x in s:
            c ^= ord(x)
        for x in t:
            c ^= ord(x)
        return chr(c) 
        
# top solution 
# store sum of ascii codes for each string
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ss, tt = 0, 0
        for x in s:
            ss += ord(x)
        for x in t:
            tt += ord(x)
        return chr(tt-ss)