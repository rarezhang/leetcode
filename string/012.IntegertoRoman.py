"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""




class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
        dic_keys = sorted(dic.keys(), key=dic.get, reverse=True)
        result = ''
        for k in dic_keys:
            quotient, num = divmod(num, dic[k]) # num = remainder 
            if quotient != 0:
                result += k*quotient
            if num == 0:
                return result
        return result
        
s = Solution()
print(s.intToRoman(3001))
         

'''
# top solution
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return ''.join((M[num/1000],C[(num%1000)/100],X[(num%100)/10],I[num%10]))
'''