class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # corner case
        if len(nums) == 0:
            return -1
        if len(nums) == 1: return nums[0]
        if len(nums) ==2:
            if nums[0]> nums[1]:
                return nums[1]
            else:
                return (nums[0])
            
        l, r = 0, len(nums)-1
        
        while l + 1 < r:
            mid = (l+r)//2
            if nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
                return nums[mid]
            elif  nums[mid] > nums[r] and nums[mid] > nums[l]:
                l = mid                
            else:
                r = mid
        if nums[l]<nums[r]:
            return  nums[l]
        else:
            return nums[r]
