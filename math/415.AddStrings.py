"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

dic = {'0': 0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) > len(num2):  # num2 longer 
            num1, num2 = num2, num1
        num1, num2 = list(num1), list(num2)
        carry, res = 0, []
        while len(num2) > 0:
            n1 = dic[num1.pop()] if len(num1) > 0 else 0
            n2 = dic[num2.pop()]
            
            temp = n1 + n2 + carry 
            res.append(temp % 10)
            carry = temp // 10
        if carry:
            res.append(carry)
        return ''.join([str(i) for i in res])[::-1]
            
s = Solution()
n1 = '1'
n2 = '9'
r = s.addStrings(n1,n2) 
print(r)       


# improvement 
dic = {'0': 0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = list(num1), list(num2)
        carry, res = 0, []
        while len(num2) > 0 or len(num1) > 0:
            n1 = dic[num1.pop()] if len(num1) > 0 else 0
            n2 = dic[num2.pop()] if len(num2) > 0 else 0
            
            temp = n1 + n2 + carry 
            res.append(temp % 10)
            carry = temp // 10
        if carry:
            res.append(carry)
        return ''.join([str(i) for i in res])[::-1]
        
        
        
# improvement 
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = list(num1), list(num2)
        carry, res = 0, []
        while len(num2) > 0 or len(num1) > 0:
            n1 = ord(num1.pop())-ord('0') if len(num1) > 0 else 0
            n2 = ord(num2.pop())-ord('0') if len(num2) > 0 else 0
            
            temp = n1 + n2 + carry 
            res.append(temp % 10)
            carry = temp // 10
        if carry: res.append(carry)
        return ''.join([str(i) for i in res])[::-1]