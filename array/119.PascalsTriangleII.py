"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""

# top solution 

# Any row can be constructed using the offset sum of the previous row. Example:
#    1 3 3 1 0 
# +  0 1 3 3 1
# =  1 4 6 4 1
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [[1]]
        for i in range(0, rowIndex):
            result = [list(map(lambda x, y: x+y, result[-1]+[0], [0]+result[-1]))]
        return result[0] 
        
s = Solution()
print(s.getRow(2))


# top solution 
# iteratively update the array from the end to the beginning.
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [0 for _ in range(rowIndex+1)]
        result[0] = 1
        for i in range(1, rowIndex+1):
            for j in range(i, 0, -1): # for(int i=1; i<rowIndex+1; i++)
                result[j] += result[j-1]
        return result
        

