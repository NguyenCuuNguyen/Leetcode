#https://leetcode.com/problems/maximum-binary-tree/description/

# # Example
# nums = [3,2,1,6,0,5]

# # The algorithm to build a tree is:
# # 1. find a maximum value of a list and store it's index
# # 2. divide a collection of list into left and right
# # 3. continue to eval the algorithm until the nums count == 0

# # Iterations
# # 1. 
# max = 6, left = [3, 2, 1], right = [0, 5]

# # 2. 
# max = 3, left = [], right = [2, 1]

# etc

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        maxIndex, root = 0, 0
        for i in range(len(nums)):
            if nums[i] > root:
                root = nums[i]
                maxIndex = i
        maxIndex = nums.index(root)
        left = self.constructMaximumBinaryTree(nums[:maxIndex])
        right = self.constructMaximumBinaryTree(nums[maxIndex+1:])
        return TreeNode(root, left, right)