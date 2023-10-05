#https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05


class Solution:
    #SOLUTION 1: Brute force O(N) time and space
    def majorityElement(self, nums: List[int]) -> List[int]:
        length = len(nums) // 3
        count = 0
        dic={}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        result = [x for x in dic if dic[x] > length]
        return result
    
    #SOLUTION 2: Boyer-Moore Majority Voting Algorithm
    def majorityElement(self, nums: List[int]) -> List[int]:
        can1, can2, count1, count2 = 0,0,0,0

        if not nums:
            return []
        for i in range(len(nums)):
            if nums[i] == can1:
                count1 += 1
            elif nums[i] == can2: #Elif bc only evaluate 1 element at a time, don't want duplicated output
                count2 += 1
            elif count1 == 0: #WHY ELIF? With if, candidate2 might be assigned duplicated val with can1, which we want to avoid especially with count1 != 0 and elif executes. Fails for [2,2]
                can1, count1 = nums[i], 1
            elif count2 == 0: #WHY ELIF? cannot evaluate can2 separately, def cause duplication upon first iteration when count2=0
                can2, count2 = nums[i], 1
            else:
                count1 -= 1
                count2 -= 1
            print(f"count1={count1} of can1={can1}, count2={count2} of can2={can2}")
        #Verification:
        
        return [num for num in (can1, can2) if nums.count(num) > len(nums) // 3]