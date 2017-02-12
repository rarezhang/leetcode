"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Subscribe to see which companies asked this question.

"""

'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Return the lowest index in the string where substring sub is found. Return -1 if sub is not found.
        return haystack.find(needle)
'''
        
# top solution 
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle)==0: return 0
        
        h = 0
        while h < len(haystack)-len(needle)+1:
            n = 0
            while n < len(needle):
                if haystack[h+n] != needle[n]:
                    break
                n += 1
            if n == len(needle):
                return h
            h += 1
        return -1 


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle: return 0
        if not haystack or len(haystack) < len(needle): return -1 
        
        h,n = 0,0
        while h < len(haystack):
            if haystack[h] == needle[n]:
                if n == len(needle)-1:
                    return h - n
                else:
                    n += 1
            elif n:  # previous char are identical but now differnt 
                h = h-n  # back to the first same character 
                n = 0
            h += 1
        return -1
        
s = Solution()
hay = "mississippi"
nee = "issip"
result = s.strStr(hay, nee)
print(result)  

# ex: haystack = "mississippi" and needle = "issip"
'''
h=0 n=0 haystack[0]=m needle[0]=i
h=1 n=0 haystack[1]=i needle[0]=i <-- same char, n++
h=2 n=1 haystack[2]=s needle[1]=s
h=3 n=2 haystack[3]=s needle[2]=s
h=4 n=3 haystack[4]=i needle[3]=i <-- same char
h=5 n=4 haystack[5]=s needle[4]=p <-- different char, go back to the last same char+1 (h=2)
h=2 n=0 haystack[2]=s needle[0]=i
h=3 n=0 haystack[3]=s needle[0]=i
h=4 n=0 haystack[4]=i needle[0]=i
h=5 n=1 haystack[5]=s needle[1]=s
h=6 n=2 haystack[6]=s needle[2]=s
h=7 n=3 haystack[7]=i needle[3]=i
h=8 n=4 haystack[8]=p needle[4]=p <-- same char and end of needle => Answer!        
'''

# pythonic 
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:  # anotehr for loop 
                return i
        return -1

       