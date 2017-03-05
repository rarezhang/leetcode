"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""

# Time Limit Exceeded 
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        k = 1
        while True:
            if k * k == x:
                return k 
            elif k * k > x:
                return k - 1
            else:
                k += 1
        return k 
                
        
# top solution 
# binary search 
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        
        left, right = 1, x
        while True:
            mid = left + (right - left) // 2  # mid * mid ? x
            if mid > x/mid:  # mid * mid > x: shrink mid 
                right = mid - 1
            else:  # mid * mid <= x
                if (mid + 1) > (x / (mid + 1)):  # mid * mid == x
                    return mid 
                left = mid + 1  # mid * mid < x
            
        
# top solution 
# newton's method 
# one starts with an initial guess which is reasonably close to the true root, 
# then the function is approximated by its tangent line 
# and one computes the x-intercept of this tangent line (which is easily done with elementary algebra). 
# This x-intercept will typically be a better approximation to the function's root than the original guess, and the method can be iterated.

"""
f'(x_n) = (y - f(x_n)) / (x_(n+1) - x_n)  --> y = 0
x_(n+1) = x_n - f(x_n) / f'(x_n)

x = sqrt(S) where S is the parameter x
x^2 = S

f(x_n) = x_n^2 - S = 0
f'(x_n) = 2 * x_n

From the first sentence,
x_(n+1) = x_n - (x_n^2 - S) / 2 * x_n
x_(n+1) = (x_n + S / x_n) / 2
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = x 
        while result * result > x:
            result = (result + x//result) // 2
        return result 
