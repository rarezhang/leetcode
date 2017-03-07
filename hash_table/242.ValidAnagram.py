"""
Given two strings s and t, write a function to determine if t is an anagram of s.
a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        for cha in s:
            dic[cha] = 1 + dic.get(cha, 0)
        for cha in t:
            if dic.get(cha) is None:
                return False
            else:
                dic[cha] = dic.get(cha) - 1
                if dic[cha] == 0:
                    del dic[cha]
        return not bool(dic)  # Empty dictionaries evaluate to False in Python:
            
sol = Solution()
s = "rat"
t = "car"

r = sol.isAnagram(s, t)
print(r)