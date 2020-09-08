class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        n = len(s)
        out, gap = '', 2*numRows - 2
        for i in range(numRows):
            tmp = i
            while tmp < len(s):
                out += s[tmp]
                if i != 0 and i != numRows - 1:
                    if tmp+gap-2*i < len(s):
                        out += s[tmp+gap-2*i]
                tmp += gap
        return out
