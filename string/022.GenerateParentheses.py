"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


"""

Backtracking is a general algorithm for finding all (or some) solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons each partial candidate c ("backtracks") as soon as it determines that c cannot possibly be completed to a valid solution

Backtracking can be applied only for problems which admit the concept of a "partial candidate solution" and a relatively quick test of whether it can possibly be completed to a valid solution.
"""
# top solution: recursive 
"""
Use two integers to count the remaining left parenthesis and the right parenthesis to be added. At each function call add a left parenthesis if remain_left>0 and add a right parenthesis if remain_right>0. Append the result and terminate recursive calls when both remain_left and remain_right are zero.
"""

class Solution(object):

    def __init__(self):
        self.result = []
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self._generate_parenthesis('', n, 0)
        return self.result
        
    def _generate_parenthesis(self, pattern, remain_left, remain_right):
        if remain_left == 0 and remain_right == 0:
            self.result.append(pattern)
            return 
        if remain_left:
            self._generate_parenthesis(pattern + '(', remain_left-1, remain_right+1)
        if remain_right:
            self._generate_parenthesis(pattern + ')', remain_left, remain_right-1)

            
# top solution:   
"""
First consider how to get the result f(n) from previous result f(0)...f(n-1).
Actually, the result f(n) will be put an extra () pair to f(n-1). Let the "(" always at the first position, to produce a valid result, we can only put ")" in a way that there will be i pairs () inside the extra () and n - 1 - i pairs () outside the extra pair.

f(0): ""
f(1): "("f(0)")"
f(2): "("f(0)")"f(1), "("f(1)")"
f(3): "("f(0)")"f(2), "("f(1)")"f(1), "("f(2)")"
So f(n) = "("f(0)")"f(n-1) , "("f(1)")"f(n-2) "("f(2)")"f(n-3) ... "("f(i)")"f(n-1-i) ... "(f(n-1)")"
"""         
class Solution(object):        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = [" "]
        
        i = 1
        while i <= n:
            pattern = []
            j = 0
            while j < i:
                for str_1 in result[j]:
                    for str_2 in result[i-1-j]:
                        pattern.append('('+str_1+')'+str_2)
                j += 1
            result.append(pattern)
            i += 1
            
        result = result[-1]
        r = []
        for s in result:
            rr = ''
            for cha in s:
                if cha != ' ':
                    rr+=cha
            r.append(rr)
        return r

            
s = Solution()
r = s.generateParenthesis(3)
print(r)


# pythonic 
class Solution(object):
    def generateParenthesis(self, n):
        def generate(p, left, right):
            if right >= left >= 0:
                if not right:
                    yield p  # right = left = 0
                for q in generate(p + '(', left-1, right): 
                    yield q
                for q in generate(p + ')', left, right-1): 
                    yield q
        return list(generate('', n, n))
        
        
# pythonic 
class Solution(object):
    def generateParenthesis(self, n):
        def generate(p, left, right, parens=[]):
            if left:         
                generate(p + '(', left-1, right)
            if right > left: 
                generate(p + ')', left, right-1)
            if not right:    
                parens += p,
            return parens
        return generate('', n, n)