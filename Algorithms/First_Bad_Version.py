"""
    n versions [1, 2, ..., n]
    bool isBadVersion(version) which returns whether version is bad
"""


class Solution:
    """Runtime: 35 ms, faster than 71.56% of Python3 online submissions for First Bad Version.
Memory Usage: 13.8 MB, less than 65.88% of Python3 online submissions for First Bad Version.
    """
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left