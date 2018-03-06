"""
566. Reshape the Matrix

In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:

Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.


Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.

Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.

"""


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # rr & cc of the given matrix 
        rr = len(nums)
        cc = len(nums[0])
        
        if r * c != rr * cc:
            return nums
        else:            
            all_n, new_nums = [], []
            for n in nums:
                all_n.extend(n)  # flat the matrix
            
            for last in range(c, len(all_n)+1, c): # range(start, stop, step)
                first = last - c
                new_rows = all_n[first: last]
                new_nums.append(new_rows)
            return new_nums


# top solution
 
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m, n = len(nums), len(nums[0])
        
        if r*c != m*n:
            return nums 
        else:
            # unpack to one row 
            items = [nn for n in nums for nn in n]
            return [items[x*c: (x+1)*c] for x in range(r)]
        



        
        
s = Solution()
nums = [[1,2],[3,4]]
# example 1
r = 1
c = 4
# example 2
# r = 2
# c = 4
# example 3 
# r = 4
# c = 1
r = s.matrixReshape(nums, r, c)       
print(r)