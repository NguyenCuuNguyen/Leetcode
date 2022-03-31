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

    """Hash table: """
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for n in range(len(nums)): #O(N)
            remain = target - nums[n] 
            if nums[n] in dic: #O(1) or worst O(N) amortized
                return [dic[nums[n]], n]
            else:
                dic[remain] = n