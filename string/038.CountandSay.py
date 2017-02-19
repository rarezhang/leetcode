"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
The "1" is the 1st string, and calculate the n th string.
"""

# top solution
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = '1'
        for _ in range(n-1):
            previous = result
            result = ''
            count = 1
            say = previous[0]
            
            i = 1
            while i < len(previous):
                if previous[i] != say:
                    result = result + str(count) + say
                    count = 1
                    say = previous[i]
                else:
                    count += 1                    
                i += 1
            result = result + str(count) + say
        return result

        
# pythonic 
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n - 1):
            # (.) captures one character and \1* covers its repetitions.
            # len(m.group(0))) --> count
            # m.group(1) --> say
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
        return s
                
                
            
solution = Solution()
for i in range(1, 10):
    print(solution.countAndSay(i))

