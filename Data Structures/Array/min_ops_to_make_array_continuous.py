# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/description/?envType=daily-question&envId=2023-10-10

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        mapp = {}
        diff = max(nums) - min(nums)
        #Check whether continuous
        if diff == len(nums) - 1:
            for num in nums:
                if num not in mapp:
                    mapp[num] = 1
            if mapp.keys() == len(nums) and all(x==1 for x in mapp.values()):
                return 0
        
        #Not continuous, start replacing:
        for num in nums:
            if num not in mapp:
                mapp[num] = 1
            else:
                mapp[num] += 1
        min_count = 0
        maxx = (len(nums)-1) + nums[0]
        nums = sorted(nums)
        window = len(nums)
        min_count = 0
        print(f"nums={nums}, mapp={mapp}")
         #FAIL BECAUSE ONLY REPLACING FROM MIN(NUMS)
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] != 1:
                if nums[i] == maxx:
                    nums[i+1] = nums[i-1]+1
                    nums = sorted(nums)
                else:
                    print(f"nums[i]={nums[i]} and nums[i-1]={nums[i-1]}")
                    nums[i] = nums[i-1] +1
                count += 1
            print(f"nums={nums}")
        return count

        #FAILED BECAUSE WE CAN CHANGE ANY NUMBER
        # for i in range(len(nums)):
        #     if curr not in mapp:
        #         print(f"curr={curr}")
        #         min_count += 1
        #     curr += 1
        # curr = nums[-1]
        # max_count = 0
        # for i in reversed(range(len(nums))):
        #     if curr not in mapp:
        #         print(f"curr={curr}")
        #         max_count += 1
        #     curr -= 1
        # return min(min_count, max_count)




        #FAIL BECAUSE ONLY REPLACING FROM MIN(NUMS)
        # for i in range(1,len(nums)):
        #     if nums[i] - nums[i-1] != 1:
        #         if nums[i] == maxx:
        #             nums[i+1] = nums[i-1]+1
        #             nums = sorted(nums)
        #         else:
        #             print(f"nums[i]={nums[i]} and nums[i-1]={nums[i-1]}")
        #             nums[i] = nums[i-1] +1
        #         count += 1
        #     print(f"nums={nums}")
        # return count

        #Fail for basic cases
        # for i in range(window):
        #     curr = nums[i]
        #     count = nums[i]
        #     for num in nums:
        #         if curr not in mapp:
        #             count -= 1
        #         curr += 1
        #     min_count = min(min_count, count)
        # return min_count