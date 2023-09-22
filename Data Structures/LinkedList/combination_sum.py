#https://leetcode.com/problems/combination-sum/description/
#39.COMBINATION SUM
class Solution:
    #1st attempt: FAIL 
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        if target < min(candidates):
            return out
        for i,can in enumerate(candidates):
            if can == target:
                out.append([can])
                print(f"added, out={out}")
            if can < target:
                #multiplier * multiplicand = product
                j = i
                sub = can
                for j,sub in enumerate(candidates[i+1:]):
                    print(f"inner loop of {can}:")
                    remainder = target % sub
                    if remainder == 0:
                        sub_list = [sub]
                        out.append(sub_list*(target//sub))
                    sub_target = target - candidates[j]
                    
                # remainder = target % can
                # if remainder == 0:
                #     sub = [can]
                #     out.append(sub*(target//can))
                # sub_target = target - candidates[i]
        return out

    #REVISIT: 
    #SOLUTION 1: DFS
    #If target becomes zero, it means a valid combination is found, so add a copy of lis to the resresres list.
    # If targettargettarget becomes negative, return because the current combination is not valid.
    # Iterate through the candidates array starting from the current index indindind.Add the current candidate value to the lislislis.
    # Recursively call the recursion function with the updated targettargettarget and lislislis.
    # Remove the last element from lislislis to backtrack and explore other possibilities.
    # After the DFS search is complete, return the resresres list containing all valid combinations.
    #[2,3,6,7]

    #MY_TAKE: use recursive function to recursively pass current element in, until either a.==target->add a copy of that list to master list, so that we can keep adding next element OR b.>target, return and pop that cur out for same reason. 
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        def DFS(index:int, array: List[int], sub_target: int) -> List[int]:
            if sub_target == target:
                out.append(array.copy())
                return
            if sub_target > target:
                return
            for i in range(index, len(candidates)):
                array.append(candidates[i])
                print(f"i={i}, array={array}, sub_target+candidates[i] ={sub_target}+{candidates[i]}")
                DFS(i, array, sub_target+candidates[i])
                array.pop()
            return array
        DFS(0, [], 0)
        return out
    #LESSON 0: find what's the repeating pattern for recursion, find terminating condition and figure out what to do next once terminated.

    #LESSON 1: to modify original input, either 1.create dummy value or 2. create helper function
    
    #LESSON 2: if a child function is defined within a parent function, child func automatically gets the parent's input, no need for self inside child's formal argument list
