"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""

class Solution(object):  # O(n*m)
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine = list(magazine)  # string is inmutable, does not have remove method
        for i in ransomNote:
            if i not in magazine:
                return False
            else:
                magazine.remove(i)  # O(n)
        return True

        
# top solutions 
class Solution(object):  # O(n+m)
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        container = [0] * 26
        a = ord('a')
        for m in magazine:
            container[ord(m)-a]+=1
        for r in ransomNote:
            container[ord(r)-a]-=1
            if container[ord(r)-a] < 0:
                return False
        return True

# pythonic 
class Solution(object):  
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        st = set(ransomNote)  # to ovid duplication 
        # alist.count()  # O(n)
        return all(ransomNote.count(r) <= magazine.count(r) for r in st)
        
from collections import Counter  
class Solution(object):   # O(m+n)
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # return not collections.Counter(ransomNote) - collections.Counter(magazine)return 
        c = Counter(magazine) # Counter->O(n)
        c.subtract(Counter(ransomNote))
        return all(cc>=0 for cc in c.values())