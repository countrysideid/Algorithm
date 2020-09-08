class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # corner case
        if len(s) <=1:
            return True
        new_s = ''
        for c in s:
            if c.isalpha() or c.isdigit():
                new_s += c.lower()
        # if len(new_s) <=1:
        #     return True
        return new_s == new_s[::-1]
                
