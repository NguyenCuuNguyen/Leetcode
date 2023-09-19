"""
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.
"""
class Solution:
    """Brute force (XX)"""
    def maxSubArray(self, nums: List[int]) -> int:
        re = -inf
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                 cur_sum += nums[j]
                 re = max(re, cur_sum)
        return re

    """Recursive (XX):
    must_pick = whether to select current element
    
    """
    def maxSubArray(self, nums: List[int]) -> int:
        def solve(i, must_pick):
            if i >= len(nums): return 0 if must_pick else -inf
            return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
        return solve(0, False)


    """Dynamic programming - Tabulation
    Base case = nums[0]
    Iterative pattern = choose bigger valuee between adding new element or the new element itself
    Return biggest value in dp 
    Runtime = O(N), Space = O(N)
    """
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for i in nums]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)

    """Divide and Conquer O(N)"""
    def maxSubArray(self, nums: List[int]) -> int:
        def divideAndConquer(i, j):
            print(f"Call with {i=} and {j=}")
            if i == j:
                return nums[i]

            k = (i+j) // 2
            res1 = divideAndConquer(i, k)
            res2 = divideAndConquer(k+1, j)

            left = leftMax = nums[k]
            for a in range(k-1, i-1, -1):
                left += nums[a]
                leftMax = max(left, leftMax)
            print(f"{leftMax=}")
            
            right = rightMax = nums[k+1]
            for a in range(k+2, j+1):
                right += nums[a]
                rightMax = max(right, rightMax)
            print(f"{rightMax=}")
            
            res3 = leftMax + rightMax
            print(f"{res3=}")
            print("##############################################")
            return max(res1, res2, res3)
        
        return divideAndConquer(0, len(nums)-1)
    

