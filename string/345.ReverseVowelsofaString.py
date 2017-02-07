"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

Subscribe to see which companies asked this question.
"""

class Solution(object):
    def reverseVowels(self, s):  # time complexity: O(2n)->O(n); space:O(n+m) n:len(s) m:len(all vowels)
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiouAEIOU'
        v = []
        for x in s:
            if x in vowels:
                v.append(x)
        s = list(s)
        for i,x in enumerate(s): # string immutable
            if x in vowels:
                s[i] = v.pop()
        return ''.join(s)

# two pointer solution 
class Solution(object):  # time complexity: O(n);  space: O(n)-> len of s 
    def reverseVowels(self, s):  # O(2n)->O(n)
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiouAEIOU'
        s = list(s)
        p1, p2 = 0, len(s)-1

        while p1 < p2:
            while s[p1] not in vowels and p1<p2:
                p1 += 1
            while s[p2] not in vowels and p1<p2:
                p2 -= 1
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1
        return ''.join(s)
        

# pythonic 
# re.findall(pattern, string, flags=0)
# Return all non-overlapping matches of pattern in string, as a list of strings. The string is # scanned left-to-right, and matches are returned in the order found.
# (?...)
# This is an extension notation of ?. The first character after the '?' determines what the meaning and further syntax of the construct is.
# re.I  or  re.IGNORECASE
# Perform case-insensitive matching; expressions like [A-Z] will match lowercase letters, too. This is not affected by the current locale and works for Unicode characters as expected.
# (?i) makes it case-insensitive
class Solution(object):
    def reverseVowels(self, s):  # O(2n)->O(n)
        """
        :type s: str
        :rtype: str
        """
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)        