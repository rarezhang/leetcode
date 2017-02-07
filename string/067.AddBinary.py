"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""


class Solution(object):  # fast
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, base=2) + int(b, base=2))[2:] # [2:] remove '0b'
        
# bin(x): Convert an integer number to a binary string. 0bxxxx
# int(x, base=10): Return an integer object constructed from a number or string x, if base is given, x must be a string

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        BASE = 2
        
        def str2num(s): # binary string to dec int
            s = reversed(s)
            r, base = 0, 1
            for i in s:
                r+=int(i)*base
                base*=BASE
            return r
        def num2str(n):  # dec int to binary string
            if n == 0: return '0'
            result = ''
            while n!=0:
                n, remainder = divmod(n, BASE)  # temp=quotient
                result += str(remainder)
            return ''.join(list(reversed(result)))    
        
        return num2str(str2num(a) + str2num(b))
        
        
            
            
        
        
        
s = Solution()
print(s.addBinary('11','11'))