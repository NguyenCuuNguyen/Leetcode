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

    