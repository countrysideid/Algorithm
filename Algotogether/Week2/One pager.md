# Find First and Last Position of Element in Sorted Array

34. https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

## Thinking Process

This is a typical binary search problem but a bit more complicated than the regular one. The framework should be binary search and since there might be multiple 
same values, we also should make sure that the first/last value should be matched with the left/right pointer.

## Solutions

### Binary search

Edge cases are checked first, if the target is less/greater than the first/last element or the nums is None, [-1, -1] is returned.
Then the binary search is used and we have to make sure that the first value that matches the target value is at the left pointer when the search is done, and 
we need to search for the last target value in the nums by adding one step on the right each time until the value is found.

## Code

### Decode String using a stack

```python
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # edge case
        if not nums:
            return [-1, -1]
        if target < nums[0] or target > nums[-1]:
            return [-1, -1]
        # if len(nums) == 1 and nums[0] == target: return [0,0]
        # if len(nums) == 1 and nums[0] = target: return [0,0]
            
        l, r = 0, len(nums)-1
        while l+1 < r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        if nums[l] == target:
            flag = l
            while l+1 < len(nums) and nums[l+1] == target:
                l+=1
            return [flag, l]
        if nums[r] == target:
            flag = r
            while r+1 < len(nums) and nums[r+1] == target:
                r+=1
            return [flag, r]

        return [-1, -1]
```

## My Weakness /Bugs

1. [Weakness-1] This is a relatively easy problem, so I do not have any weakness.

2. [Bug-1] This is a relatively easy problem, so there is no bug.

## My Similar Problems

