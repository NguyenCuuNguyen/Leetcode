"""
:type nums1: List[int]
:type nums2: List[int]
=> return an array of their intersection, in any order
"""
class Solution:


    """HASHTABLE: 
    O(N^N): in is O(N) inside for loop"""
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

    
    """
    Counter = O(n1) + O(n2)
    + O(len(intersection)) => ignore
    + get dict O(n1)* len(intersection)
    => ~O(n) 
    96 ms, faster than 19.39% . 14.2 MB, less than 17.95%"""
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        re = []
        count1 = collections.Counter(nums1)
        count2 = collections.Counter(nums2)
        keylist = list(set(nums1) & set(nums2))
        for k in keylist:
            re.extend(list([k] * min(count1.get(k), count2.get(k))))
        return re


    """Binary search:
    
    /*
nums1 = [1,2,2,1], nums2 = [2,2]

1,1,2,2
2,2

nums1 = [4,9,5], nums2 = [9,4,9,8,4]

4,4,8,9,9
4,5,9


--

main idea:

using binary search, search for the elements of the smallest array (nums1) in the largest array (nums2)

sort the largest array o that binary search is feasible
sort the smallest array so that we can seach sequentially

if element is found,
	keep searching to the left until we find the first occurrence of the element

	add element to the result

when element is found, keep track of the last index where element was found so that next binary search ignores previous used indexes
	ie. nums1 = 1,1   nums2 = 1,2,2 - output should be [1] - once we found first 1 at index 0 and next search is done as of index 1

*/
https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/1808056/Java-Binary-Search
    """