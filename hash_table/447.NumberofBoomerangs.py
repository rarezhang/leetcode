"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""


# top solution: O(n**2)
# for each point, create a hashmap and count all points with same distance. 
# If for a point p, there are k points with distance d, number of boomerangs corresponding to that are k*(k-1). 
# Keep adding these to get the final result.

# Time Limit Exceeded
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def distance(A, B):
            #return ((A[0]-B[0])**2 + (A[1]-B[1])**2) ** 0.5 
            return (A[0]-B[0])**2 + (A[1]-B[1])**2
            
        
        result = 0
        for p_a in points:
            dic = {}
            for p_b in points:
                if p_a == p_b:
                    continue
                s = distance(p_a, p_b)
                dic[s] = 1 + dic.get(s, 0)
            for k in dic:
                if dic[k] > 1:
                    result += dic[k] * (dic[k] - 1)
        return result 
            
        
        
sol = Solution()
r = sol.numberOfBoomerangs([[0,0],[1,0],[2,0]])       
print(r) 