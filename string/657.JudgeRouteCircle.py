"""
657. Judge Route Circle

Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
"""

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        a_dic = {}
        M = "RLUD"
        for m in M:
            a_dic[m] = 0
            
        for mo in moves:
            a_dic[mo] += 1        
        
        """
        if a_dic["R"] == a_dic["L"] and a_dic["U"] == a_dic["D"]:
            return True 
        else:
            return False
        """    
        return a_dic["R"] == a_dic["L"] and a_dic["U"] == a_dic["D"]


        
# top solution 
import collections
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        c = collections.Counter(moves)
        return c['L'] == c['R'] and c['U'] == c['D']


class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # not very efficient --> O(4n)
        # string.count() --> O(1)
        return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")
        
            
s = Solution()
mm = "UD"
mm = "LL"
r = s.judgeCircle(mm)    
print(r)    
