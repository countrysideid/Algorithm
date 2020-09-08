'''python
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # corner case
        str = str.lstrip()
        if not str:
            return 0
        num = 0
        length = len(str)
        if str[0].isdigit():
            p = 0
            while p < length and str[p].isdigit() :
                num = num * 10 + int(str[p])
                p+=1
            if num > 2**31 - 1:
                return 2**31 - 1
            if num <= -2**31:
                return  -2**31
            return num
        elif   str[0] == '+' :
            p = 1
            while p < length and str[p].isdigit():
                num = num * 10 + int(str[p])
                p+=1
            if num > 2**31 - 1:
                return 2**31 - 1
            if num <= -2**31:
                return  -2**31
            return num
        elif str[0] == '-' :
            p = 1
            while  p < length and str[p].isdigit():
                num = num * 10 + int(str[p])
                p+=1
            num  = - num
            if num > 2**31 - 1:
                return 2**31 - 1
            if num <= -2**31:
                return  -2**31
            return num
        else:
            return 0

'''
