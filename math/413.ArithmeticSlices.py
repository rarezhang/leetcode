"""
A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
"""

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        curr, sum = 0, 0
        for i in range(2, len(A)):
            if A[i]-A[i-1]==A[i-1]-A[i-2]:
                curr+=1
                sum+=curr
            else:
                curr=0
        return sum
            
"""
i) We need minimum 3 indices to make arithmetic progression,
ii) So start at index 2, see if we got two diffs same, so we get a current 1 arith sequence
iii) At any index i, if we see it forms arith seq with former two, that means running (curr) sequence gets extended upto this index, at the same time we get one more sequence (the three numbers ending at i), so curr++. Any time this happens, add the curr value to total sum.
iv) Any time we find ith index does not form arith seq, make currently running no of seqs to zero.
"""