#https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
class Solution:
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