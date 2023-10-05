#https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #array element's value = maximum number of jumps you can make. E.g, if element = 3, can do 1,2 or 3 jumps
        #Intuition: reverse engineer and read the array backwards, if num == distance to nums[-1], getting to num from head of list is new goal
        if len(nums) == 1:
            return True
        targetIdx = len(nums)-1

        for i in reversed(range(len(nums)-1)):
            print(f"i={i}, nums[i]={nums[i]}, i+nums[i]={i+nums[i]}")
            if i+nums[i] >= targetIdx:
                #Has to be >= and not ==, because would fail with input [2,0]. We can jump < than the element value
                targetIdx = i
        return True if targetIdx == 0 else False
            #if nums[num] == 0: #cannot move forward

#LESSON: Don't over complicate things, just stay as close as possible to the prompt and translate into algorithm using prompt.