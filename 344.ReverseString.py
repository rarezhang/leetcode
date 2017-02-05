"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""

# get memory issue when handling long string
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        else:
            return self.reverseString(s[1:]) + s[0]

# better recursion method 
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length < 2:
            return s
        else:
            return self.reverseString(s[length/2:]) + self.reverseString(s[:length/2])

# swap  
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)  # Python strings immutable
        i, j = 0, len(l)-1
        while i < j:
            l[i], l[j] = l[j], l[i]  # swap
            i += 1
            j -= 1
        return ''.join(l)
        


# python extended slices --> fastest
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
        

# python reversed() method
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # reversed() return an object
        return ''.join(list(reversed(s)))