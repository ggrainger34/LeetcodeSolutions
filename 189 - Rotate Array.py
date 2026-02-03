"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % len(nums)
        if k != 0:
            nums[:k], nums[k:] = nums[n-k:], nums[:n-k]
