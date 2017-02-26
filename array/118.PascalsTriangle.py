"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

# top solution 
# Any row can be constructed using the offset sum of the previous row. Example:
#    1 3 3 1 0 
# +  0 1 3 3 1
# =  1 4 6 4 1

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1]]
        for i in range(1, numRows):
            result += [list(map(lambda x, y: x+y, result[-1]+[0], [0]+result[-1]))]
        return result[:numRows]
        
s = Solution()
s.generate(5)

# top solution 
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        all_rows, row = [], []
        for i in range(numRows):
            row = [1] + row  # left append
            for j in range(1, len(row)-1):
                row[j] = row[j] + row[j+1]
            all_rows.append(row)
        return all_rows

        
# top solution
# two loops, one go through the row, one go through the column
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        all_rows = [None] * numRows
        for i in range(numRows):
            all_rows[i] = [None] * (i+1)
            all_rows[i][0] = all_rows[i][i] = 1
            for j in range(1, i):
                all_rows[i][j] = all_rows[i-1][j-1] + all_rows[i-1][j]
        return all_rows        