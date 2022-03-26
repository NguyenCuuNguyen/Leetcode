"""
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.
"""
class Solution:
    """Brute force (X)"""
    def maxSubArray(self, nums: List[int]) -> int:
        re = -inf
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                 cur_sum += nums[j]
                 re = max(re, cur_sum)
        return re