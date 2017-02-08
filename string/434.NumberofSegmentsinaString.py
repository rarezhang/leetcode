"""
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.
"""


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
        
        
def countSegments(self, s):  # the first char of a token -> how many chars in total -> how many segments
        return sum([s[i] != ' ' and (i == 0 or s[i - 1] == ' ') for i in range(len(s))])