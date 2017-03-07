"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""
row1 = 'qwertyuiop'
row2 = 'asdfghjkl'
row3 = 'zxcvbnm'

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for w in words:
            if w in row1:
                result.append('1')
            elif w in row2: 
                result.append('2')
            elif w in row3:
                result.append('3')
        return len(set(result)) == 1