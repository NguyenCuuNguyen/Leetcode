class Solution:
    """O(N^2)"""
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for n in range(len(nums)):
            x = target - nums[n]
            if x in nums and nums.index(x) != n:
                res.append(n)
                res.append(nums.index(x))
                return res