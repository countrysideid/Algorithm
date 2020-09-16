class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        # edge case
        if dividend == 0:
            return 0
        
        neg = (dividend <0 ) != (divisor <0)
        
        dividend = left = abs(dividend) 
        divisor = right = abs(divisor)
        ans = 0          
        Q = 1

        while left >= divisor:
            left -= right
            ans += Q
            Q += Q
            right += right
            if left < right:
                right = divisor
                Q= 1
        if neg:
            return max(-ans, -2147483648)
        else:
            return min(ans, 2147483647)
            
           
