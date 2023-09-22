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
    
    #Success 2: Binary search but 2 while loops O(logN)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        head, tail = 0, len(nums)-1
        output = [-1,-1]
        while head <= tail:
            mid = head + (tail-head)//2
            print(f"mid={mid}, head={head}, tail={tail}")
            if nums[mid] == target:
                output[0] = mid
            if nums[mid] < target:
                head = mid+1
            else:
                tail = mid-1
        tail = len(nums)-1
        while head <= tail:
            mid = head + (tail-head)//2
            if nums[mid] == target:
                output[1] = mid      
            if nums[mid] > target:
                tail = mid-1 
            else:
                head = mid+1
        return output
    #LESSON 0: Search in sorted array, use binary search
    #LESSON 1: In binary search, use separate "if conditions" to evaluate == and either > or < instead of group = and > or< together
    #LESSON 2: in the second if (after confirming middle !=target), if evaluate for the opposite direction first (i.e.,> for first output), we will miss the case [5,7,7,8,8,10] because we're moving head up & evaluating the bigger half, instead of the desired smaller half. Similarly with the other direction