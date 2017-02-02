"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 = x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
"""


from itertools import izip
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        max_num = max(x, y)
        assert max_num < 2**31

        if max_num < 2**4 - 1:
            st = ''.join(('{0:0','4','b}'))            
        elif max_num < 2**8 -1:
            st = ''.join(('{0:0','8','b}'))
        elif max_num < 2**16 -1:
            st = ''.join(('{0:0','16','b}'))
        else:
            st = ''.join(('{0:0','32','b}'))
        x, y = st.format(x), st.format(y)  # {0:04b}.format(x)
        return sum(xx!=yy for xx, yy in izip(x, y))
        
# top solution 
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')
