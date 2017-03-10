"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

# top solution 
# sliding window 
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # init a collection or int value to save the result according the question.
        result = []
        
        if len(s)==0 or len(p)==0 or len(s)<len(p):
            return result
            
        # create a hashmap to save the Characters of the target substring        
        dic = {}        
        # record each character in p 
        # (K, V) = (Character, Frequence of the Characters)
        for x in p:
            dic[x] = 1 + dic.get(x, 0)         

        # maintain a counter to check whether match the target string
        # must be the map size, NOT the string size because the char may have duplicate.
        count = len(dic)    
        
        # two pointers 
        # begin - left pointer of the window; end - right pointer of the window
        left, right = 0, 0
        
        # loop through the soruce string 
        while right < len(s):
            # get a character 
            char = s[right]
            
            # move right evertime if the character exists in p's hash, decrease the count current hash value means the character is existing in p
            if char in dic:
                dic[char] = dic.get(char) - 1
                if dic.get(char) == 0:
                    count -= 1
                
            right += 1

            # when the count is down to 0, means we found the anagram, then add window's left to result list
            while count == 0:                
                temp = s[left]
                if temp in dic: # only increase the count if the character is in p
                    # reset the hash because we kicked out the left                
                    dic[temp] = dic.get(temp) + 1
                    if dic.get(temp) > 0: # the count > 0 indicate it was original in the hash, cuz it won't go below 0
                        count += 1
                
                # if  we find the window's size equals to p, then we have to move left (narrow the window) to find the new match window                
                if right - left == len(p):
                    result.append(left)
                    
                left += 1 # narrow the window
                
        return result 

        
        
sol = Solution()
s = "cbaebabacd"
p = 'abc'
r = sol.findAnagrams(s, p)
print(r)
