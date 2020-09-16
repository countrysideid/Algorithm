class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # corner case
        if not nums:
            return -1
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums)-1
    
        l, r = 0, len(nums)-1
        while l+1 < r:
            mid = (l+r) //2
            if nums[mid] > nums[mid+1] and nums[mid]> nums[mid-1]:
                return mid
            elif nums[mid] > nums[mid+1] and nums[mid]< nums[mid-1]:
                r = mid
            else:
                l = mid

        
