"""
:type nums1: List[int]
:type nums2: List[int]
=> return an array of their intersection, in any order
"""
class Solution:


    """O(N^N): in is O(N) inside for loop"""
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}         
        for num in nums1:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        re = []    
        for v in nums2:
            if v in d and d[v] > 0:
                re.append(v)
                d[v] -= 1
        return re

    
    """96 ms, faster than 19.39% . 14.2 MB, less than 17.95%"""
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        re = []
        count1 = collections.Counter(nums1)
        count2 = collections.Counter(nums2)
        keylist = list(set(nums1) & set(nums2))
        for k in keylist:
            re.extend(list([k] * min(count1.get(k), count2.get(k))))
        return re