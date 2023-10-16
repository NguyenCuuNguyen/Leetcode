class Solution:
    #Time O(N)
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        #basecase
        if len(nums) == 1:
            return [nums[:]]
        
        for num in range(len(nums)):
            n = nums.pop(0)
            print(f"after pop, list={nums}")
            perms = self.permute(nums)
            print(f"perms={perms}")
            for perm in perms:
                perm.append(n)
            ans.extend(perms)
            print(f"ans={ans}")
            nums.append(n) #backtrack
            print(f"nums={nums}\n")

        return ans

#Need fixing REVIEW
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def permutation(nums: List[int], start:int, end:int) ->  List[int]:
            nonlocal ans
            if start == end:
                ans.append(nums)
                print(f"ans={ans}, nums={nums}")
                return ans
            else:
                for i in range(start, end):
                    nums[start], nums[i] = nums[i], nums[start]
                    permutation(nums, start+1, end)
                    nums[start], nums[i] = nums[i], nums[start]
        permutation(nums,0,len(nums))
        print(ans)
        return ans
    

    def permutation(list, start, end):
        if start == end:
            print(list)
        else:
            for i in range(start, end+1):
                print(f"before swapping index{start}=list[start]={list[start]} and index={i}=list[i]={list[i]}")
                list[start], list[i] = list[i], list[start]
                self.permutation(list, start + 1, end)
                print(f"BEFORE swapping BACK list[start]={list[start]} and list[i]={list[i]}")
                list[start], list[i] = list[i], list[start]
                print(f"AFTER swapping BACK list[start]={list[start]} and list[i]={list[i]}\n")

    permutation([1,2,3],0,2)




# class Solution:
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     ans = []
    #     used = []
    #     def backtrack(self, res: List[int], nums: List[int], permutation:List[int], used:List[int]) -> List[int]:
    #         if len(permutation) == len(nums):
    #             ans.append(permutation)
    #             return permutation

    #         for i in range(len(nums)):
    #             if not used[nums[i]]:
    #                 used.append(nums[i])
    #                 permutation.append(nums[i])
    #                 used.pop(nums[i])
    #                 permutation.pop(nums[i])
    #     backtrack(ans, nums,[],[])
        