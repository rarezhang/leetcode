"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        p = len(s) - 1
        result = []
        while p > -1 and not s[p].isalpha():
            p -= 1
        while p > -1 and s[p].isalpha():
            result.append(s[p])
            p -= 1
        return len(result)
        
solution = Solution()
test = 'Hello, world'
test = 'a'
print(solution.lengthOfLastWord(test)) 


# pythonic 
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(' ')[-1])       