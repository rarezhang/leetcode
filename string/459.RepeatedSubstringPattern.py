"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:
Input: "aba"
Output: False

Example 3:
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""

class Solution(object):  # O(n*log(n))
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        length = len(str)
        for i in range(length//2,0,-1):  # length//2 ~ 1
            if length % i == 0:  # there is the possibility 
                sub = str[:i]
                temp = ''
                while len(temp) < length:
                    temp = ''.join((temp, sub))
                if str == temp: return True
        return False
            


# top solutions   O(n)
# KMP issue: the Knuth–Morris–Pratt string searching algorithm (or KMP algorithm) searches for occurrences of a "word" W within a main "text string" S by employing the observation that when a mismatch occurs, the word itself embodies sufficient information to determine where the next match could begin, thus bypassing re-examination of previously matched characters.
class Solution(object):  # O(n)
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        def kmp_table(s):            
            partial_match_table = [0]*length
            s = list(s)
            i,j=0,1
            while i<length and j<length:
                if s[i]==s[j]:
                    partial_match_table[j]=i+1
                    i+=1
                    j+=1
                else:
                    if i==0:
                        partial_match_table[j]=0
                        j+=1
                    else:
                        i = partial_match_table[i-1]
            return partial_match_table
            
        length = len(str)
        prefix = kmp_table(str)
        n = prefix[length-1]
        return (n>0) and (length%(length-n)==0)  
        # in the partial_match_table, the number means longest prefix and also suffix. So (length-n): the length of the prefix(should be the repeated sequence), (length%(length-n)==0): check if the candidate sequence is the answer(if it is the answer, the array should not have remains).


        
# pythonic 
class Solution(object):  
    def repeatedSubstringPattern(self, str):
            """
            :type str: str
            :rtype: bool
            """           
            # ss = (str + str)[1:-1]  # s[1:-1] no first and last character
            # return ss.find(str) != -1
            return str in (2 * str)[1:-1]

"""
Consider a string S="helloworld". Now, given another string T="lloworldhe", can we figure out if T is a rotated version of S? Yes, we can! We check if S is a substring of T+T.

Fine. How do we apply that to this problem? We consider every rotation of string S such that it's rotated by k units [k < len(S)] to the left. Specifically, we're looking at strings "elloworldh", "lloworldhe", "loworldhel", etc...

If we have a string that is periodic (i.e. is made up of strings that are the same and repeat R times), then we can check if the string is equal to some rotation of itself, and if it is, then we know that the string is periodic. Checking if S is a sub-string of (S+S)[1:-1] basically checks if the string is present in a rotation of itself for all values of R such that 0 < R < len(S).
"""
            
            
            
s = Solution()        
inputs = ["a","abab","aba","abcabcabcabc", "ababab"]

for i in inputs:
    print(s.repeatedSubstringPattern(i))