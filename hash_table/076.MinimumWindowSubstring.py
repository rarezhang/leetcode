"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""
import sys
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        
        # create a hashmap to save the Characters of the target substring        
        dic = {}        
        # record each character in p 
        # (K, V) = (Character, Frequence of the Characters)
        for x in t:
            dic[x] = 1 + dic.get(x, 0)

        # maintain a counter to check whether match the target string
        # must be the map size, NOT the string size because the char may have duplicate.
        count = len(dic)

        # two pointers 
        # begin - left pointer of the window; end - right pointer of the window
        left, right = 0, 0
        head = 0
        
        # the length of the substring which match the target string.
        length = sys.maxint; 
        
        # loop through the source string 
        while right < len(s):
            # get a character 
            char = s[right]
            
            # if the character exists in the hash table, decrease the count 
            if char in dic:
                dic[char] = dic.get(char) - 1
                if dic.get(char) == 0:
                    count -= 1
            right += 1
            
            # when the count is down to 0, found the substring 
            while count == 0:
                temp = s[left]
                if temp in dic:
                    # only increase the count if the character is in p
                    # reset the hash because we kicked out the left                
                    dic[temp] = dic.get(temp) + 1
                    if dic.get(temp) > 0: # the count > 0 indicate it was original in the hash, cuz it won't go below 0
                        count += 1
                if right - left < length:
                    length = right - left
                    head = begin 
                left += 1
        
        if length == sys.maxint:
            return ""
        return s[head:head+length]