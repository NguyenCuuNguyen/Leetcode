#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

class Solution:
    #Success 1: Brute force - Iterate through all element O(N) and take care of edge cases later
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i,num in enumerate(nums):
            if num == target:
                output.append(i)
                print(f"adding at index{i}")
        if len(output) == 0:
            output = [-1, -1]
        elif len(output) == 1:
            output = output * 2
        output = output[::len(output)-1]
        return output