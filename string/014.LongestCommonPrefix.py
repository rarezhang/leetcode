"""
Write a function to find the longest common prefix string amongst an array of strings.
example:
[] -> ''
['a'] -> 'a'
['aa', 'a'] -> 'a'
["a","a","b"] -> ''
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        if not strs:  # empty strs
            return prefix 
        # check char by char; for each char, check all the string 
        for i,char in enumerate(strs[0]):
            for s in strs[1:]:  # start with the 2nd string
                if i > len(s)-1 or char != s[i]:
                    return prefix
            prefix += char
        return prefix

l = ["aa", 'a']
ss = Solution()
res = ss.longestCommonPrefix(l)
print(res)



# pysonic 
# use zip 
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
            
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:  # set(lettr_group)==1: all strings have same prefix
                return strs[0][:i]

        return min(strs)
        


# pythonic: reduce
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def common_prefix(short_str, long_str):
            if len(short_str)>len(long_str):
                short_str, long_str = long_str, short_str
            for i in range(len(short_str)):
                if short_str[i] != long_str[i]:
                    return short_str[:i]
            return short_str
            
        return reduce(common_prefix, strs) if strs else ""
  
    
    
    
    

            