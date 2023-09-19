#https://leetcode.com/problems/invert-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Intuition:
# In this question we have to Invert the binary tree.
# So we use Post Order Treversal in which first we go in Left subtree and then in Right subtree then we return back to Parent node.
# When we come back to the parent node we swap it's Left subtree and Right subtree.
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        self.invertTree(root.left)
        self.invertTree(root.right)
        #Swap major left and right branches
        root.left, root.right = root.right, root.left
        return root
        
        