#https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    #SOLUTION 1: hash map, Brute force Time O(N), space O(N)
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 0
            else:
                dic[n] += 1
        answer = max(zip(dic.values(), dic.keys()))
        print(answer[1])
        return answer[1]
    
    #SOLUTION 2: Sorting, Time O(N), space O(1)
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        mid = len(nums) //2
        nums = sorted(nums)
        return nums[mid]


    #SOLUTION 3: MOORE Voting algorithm Time O(N), space O(1) but only iterate through original array once
    #
    def majorityElement(self, nums: List[int]) -> int:
        can, count = None, 0
        for n in nums:
            print(f"before, count={count}, n={n}, can={can}")
            if count == 0:
                can = n
            if n == can:
                count += 1
            else:
                count -= 1
            print(f"-----> after, count={count}, n={n}, can={can}\n")
        return can