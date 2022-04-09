class Solution:
    """Naive O(N)"""
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqr_ar = [x**2 for x in nums]
        return sorted(sqr_ar)


    """2 Pointers"""
    def sortedSquares(self, nums: List[int]) -> List[int]:
        head, tail = 0, len(nums)-1
        res = [None for _ in nums]

        for i in range(len(nums)-1, -1, -1):
            if abs(nums[head]) < abs(nums[tail]):
                res[i] = nums[tail]**2
                tail -= 1
            else:
                res[i]=nums[head]**2
                head += 1
        return res