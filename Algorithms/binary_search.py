class Solution:
    """Runtime: 369 ms, faster than 31.18% of Python3 online submissions for Binary Search.
Memory Usage: 15.3 MB, less than 99.54% of Python3 online submissions for Binary Search."""
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        print(l)
        half = nums[l//2]
        half_index = l//2
        print(f"{half=} at index {l//2}")
        if half < target:
            #upper half:
            for i in range(half_index, len(nums)):
                print(f"{nums[i]=}")
                if nums[i] == target:
                    return i
            return -1
        elif half > target:
            for i in range(0, half_index):
                if nums[i] == target:
                    return i
            return -1
        elif half == target:
            return half_index
        else:
            return -1
            
    