# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

#arr[0]-->arr[i]: ascending order
#arr[i] --> arr[len(arr)-1]: descding order
#=> Return min index of target
#Time: O(log N) => Binary search

#SOLUTION 1: Binary search to find peak, then binary search again for each half of the mountain for target:
class Solution:
    def binarySearch(self, target:int, start:int, end:int, mountain_arr: 'MountainArray', reverse:bool) -> int:
        while start != end:
            mid = (end + start) //2
            mid_val = mountain_arr.get(mid)
            print(f"start={start}, end={end}, mid={mid}, mid_val={mid_val}")
            if not reverse:
                if mid_val < target: #
                    start = mid + 1
                elif mid_val > target:
                    end = mid
                else: 
                    return mid
            else:
                if mid_val < target:
                    end = mid
                elif mid_val > target:
                    start = mid + 1
                else:
                    return mid
        return start


    def findPeak(self, start:int, end:int, mountain_arr:'MountainArray') -> int:
        while start != end:
            midIdx = start + (end-start) //2  #why inide?
            if mountain_arr.get(midIdx) < mountain_arr.get(midIdx+1): #not actually peak, move further along right side
                start = midIdx+1
            else: #check left side = ascending slope
                end = midIdx
        return start
                

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        peakInx = self.findPeak(1, n-2, mountain_arr)
        #search for target in the first ascending half:
        increasing_idx = self.binarySearch(target, 0, peakInx, mountain_arr, False)
        print(f"increasing_idx={increasing_idx}")
        if mountain_arr.get(increasing_idx) == target:
            return increasing_idx
        decreasing_idx = self.binarySearch(target, peakInx, n-1, mountain_arr, True)
        print(f"decreasing_idx={decreasing_idx}")
        if mountain_arr.get(decreasing_idx) == target:
            return decreasing_idx
        return -1

class Solution:
    #First attempt: passed 14/79 cases, failed at n=3
    def binarySearch(self, target:int, start:int, end:int, mountain_arr: 'MountainArray') -> int:
            mid = (end + start) //2
            print(f"end={end}, start={start}, mid={mid}")
            mid_val = mountain_arr.get(mid)
            if end>=start:
                if mid_val < target:
                    #search right: 
                    return self.binarySearch(target, mid+1, end, mountain_arr)
                elif mid_val > target:
                    print(f"Call binarysearch on start={start}, end={mid-1}")
                    return self.binarySearch(target, start, mid-1, mountain_arr)
                else:
                    return mid
            else:
                return -1


    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        start = mountain_arr.get(0)
        fifth = mountain_arr.get(n//5)
        two_fifth = mountain_arr.get((n//5)*2)
        mid = mountain_arr.get((n//5)*3)
        four_fifth = mountain_arr.get((n//5)*4)
        end = mountain_arr.get(n-1)
        print(f"n={n}, start={start}, fifth={fifth}, two_fifth={two_fifth}, mid={mid}, four_fifth={four_fifth}, end={end}")

        if target <= fifth:
            ans = self.binarySearch(target, start, fifth, mountain_arr)
            #Search the right side if the ans == -1, whatabout descending order?
            if ans == -1:
                print(f"binary search on start={mid}, end={end}")
                ans = self.binarySearch(target, mid, end, mountain_arr)
        else:
            print(f"binary search on start={fifth}, end={mid}")
            ans = self.binarySearch(target, fifth, mid, mountain_arr)
            print(f"after search descending half, ans={ans}")
        return ans