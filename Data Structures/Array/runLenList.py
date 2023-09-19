class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #range(start, stop. step)
        array = []
        for i in range(1, len(nums), 2):
            #Without outer bracket, error "int obj is not iterable"
            array += [nums[i]] * nums[i-1]
        return array
