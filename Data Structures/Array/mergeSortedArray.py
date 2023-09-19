class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        """sort: O(m+n log m+n) + list_get_slice: O(n)"""
        nums1[len(nums1)-n:] = nums2
        nums1.sort()


    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #Compare from the back for ease of switching position
        #Decrement index if element is larger:
        #Tail is incremented, fill in values
        #No switching between elements, just overwrite
        i = m-1
        j = n-1
        tail = m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[tail] = nums2[j]
                j -= 1
                tail -= 1
            elif nums2[j] < nums1[i]:
                nums1[tail] = nums1[i]
                i -=1
                tail -= 1
            else:
                nums1[tail] = nums1[i]
                nums1[tail-1] = nums2[j]
                i -= 1
                j -= 1
                tail -= 2
        #In cases m = 0, n >0:        
        while j >= 0:
            nums1[tail] = nums2[j]
            j -= 1
            tail -= 1