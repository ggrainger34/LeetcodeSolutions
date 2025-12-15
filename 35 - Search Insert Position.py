"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        r = len(nums) - 1 # Find the last index
        l = 0 # The first index
        if target > nums[r]:
            return r + 1
        if target < nums[l]:
            return 0

        while True:
            m = (r + l) // 2 # Calculate midpoint
            if target == nums[m]:
                return m
            if r - l == 1:
                return r
            # If target is less than midpoint
            if target < nums[m]:
                r = m
            # If target is greater than the midpoint
            if target > nums[m]:
                l = m