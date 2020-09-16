class Solution(object):
    def smallestDivisor(self,nums, threshold) :
        def condition(divisor) :
            return sum((num - 1) // divisor + 1 for num in nums) <= threshold

        left, right = 1, sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
