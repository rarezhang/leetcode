"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Subscribe to see which companies asked this question.
"""

'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []  # last in first out 
        
        left, right = '({[', ')}]'
        for cha in s:
            if cha in left:
                stack.append(cha)  # stack.pop()
            if cha in right:
                if len(stack)<1:
                    return False
                left_cha = stack.pop()
                if left.index(left_cha) != right.index(cha):
                    return False
        return stack == []
                



# top solution 
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []  # stack.append = stack.push
        for cha in s:
            if cha == '(':
                stack.append(')')  
            elif cha == '[':
                stack.append(']')
            elif cha == '{':
                stack.append('}')
            elif cha in ')]}' and (len(stack)==0 or cha != stack.pop()):
                return False
        return len(stack)==0 
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []  # last in first out 
        dic = {')':'(', ']':'[', '}':'{'}
        #right = dic.keys()  # O(n) in python 2; O(1) in python 3 -> generator 
        #left = dic.values()
        for cha in s:
            if cha in dic.values():
                stack.append(cha)
            elif cha in dic.keys():
                if stack == [] or dic[cha]!=stack.pop():
                    return False
        return stack == []

s = Solution()
test = '['
result = s.isValid(test)    
print(result)        