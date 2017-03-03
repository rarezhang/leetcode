"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.

"""
# python has no overflows 


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        temp = [] 
        if x < 0:
            x = -x
            flag = True
        else: # x>0
            flag = False            

        while x > 0:
            temp.append(x%10)
            x //= 10
        for i in temp:
            result = result*10 + i 
        if flag: result = -result  
        if -2**31 < result < 2**31-1: 
            return result 
        else:
            return 0

s = Solution()
t = s.reverse(-2147483648) 
print(t)   
        
            
# improve based on top solution 
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """        
        if x < 0:
            x = -x
            flag = True
        else: # x>0
            flag = False 
            
        result = 0
        while x != 0:
            tail = x % 10
            new_result = result * 10 + tail
            if new_result > 2**31-1:
                return 0
            result = new_result
            x = x/10
        return -result if flag else result 