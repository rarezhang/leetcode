"""
557. Reverse Words in a String III

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.

"""
'''
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split() 
        return ' '.join(w[::-1] for w in s_list)
        """
        for w in s_list:
            reverse_w = w[::-1]
        """    
'''

# top solution
# first reverse the order of the words and then reverse the entire string.        
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # print(s.split()[::-1]) # ['contest', 'LeetCode', 'take', "Let's"]
        # ' '.join(s.split()[::-1])[::-1] # s'teL ekat edoCteeL tsetnoc
        return ' '.join(s.split()[::-1])[::-1]

        
sol = Solution()
s = "Let's take LeetCode contest"
r = sol.reverseWords(s)
print(r)        