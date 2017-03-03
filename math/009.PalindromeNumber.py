"""
Determine whether an integer is a palindrome. Do this without extra space.

palindrome: a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        return x == x[::-1]

s = Solution()
s.isPalindrome(0)

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        left, right = 0, len(x)-1
        while left < right:
            if x[left] != x[right]:
                return False
            else:
                left += 1
                right -= 1
        return True   

# top solution 
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0) or (x!=0 and x%10==0):
            return False
        reverse = 0
        while x > reverse:
            reverse = reverse*10 + x%10
            x = x//10
            #print(x, reverse)
        return x==reverse or x==reverse//10
        # if len(x) is even: test x==reverse
        # e.g., 12332 1
        #       1233 12
        #       123 123
        # return True
        # --------------------------
        # if len(x) is odd: test x==reverse//10
        # 1232 1
        # 123 12
        # 12 123
        # True

        
        
s = Solution()
r = s.isPalindrome(123321)
print(r)