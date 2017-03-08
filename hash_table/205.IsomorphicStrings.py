"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length
"""


# top solution 
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic_s, dic_t = {}, {}
        for i, x in enumerate(s):
            dic_s[x] = dic_s.get(x, []) + [i]
        for i, x in enumerate(t):
            dic_t[x] = dic_t.get(x, []) + [i]
        return sorted(dic_s.values() == sorted(dic_t.values())



# top solution 
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # ascii extended table --> 256 in total 
        d1 = [[] for _ in range(256)]  
        d2 = [[] for _ in range(256)]
        for i, x in enumerate(s):
            d1[ord(x)].append(i)
        for i, x in enumerate(t):
            d2[ord(x)].append(i)
        return sorted(d1) == sorted(d2) 
        


# top solution 
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1, d2 = [0 for _ in xrange(256)], [0 for _ in xrange(256)]
        for i in xrange(len(s)):
            if d1[ord(s[i])] != d2[ord(t[i])]:
                return False
            d1[ord(s[i])] = i+1
            d2[ord(t[i])] = i+1
        return True
        
sol = Solution()
s = "ab"
t = "aa"
r = sol.isIsomorphic(s, t)
print(r)