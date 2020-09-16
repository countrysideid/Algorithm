class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x==1:
            return x
        r = 1
        while r**2<=x:
            r *= 2
        l,r = r/2, r
        while l+1 < r:
            mid = (l+r)//2
            if mid**2 == x:
                return mid
            elif mid**2 > x:
                r = mid
            else:
                l = mid
        if r ** 2 > x:
            return l
        else:
            return r
                
        
        
