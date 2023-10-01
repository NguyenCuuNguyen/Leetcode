#https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/?envType=study-plan-v2&envId=top-interview-150
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #SOLUTION 1 WORKS!
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #postorder always has root as the last node in the list left, right and root
        # in order has left subtree, root, right subtree
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        print(f" root={root}, inorder={inorder}, indexroot={inorder.index(root.val)}\n")
        rootIndexIn = inorder.index(root.val) 
        leftSize = len(inorder[0:rootIndexIn])
        root.left = self.buildTree(inorder[:rootIndexIn], postorder[:leftSize] )
        root.right = self.buildTree(inorder[rootIndexIn+1:], postorder[leftSize:len(postorder)-1])
        #why not return TreeNode(root, leftTree, right Tree)? because none of the node will be completed during recursive calls
        return root

    #SOLUTION 2: 
    #We start by creating a hashmap called inorder_map to store the indices of each element in the inorder list. This will allow us to quickly find the index of a given value in constant time later on.
    # Then, we define a recursive helper function called build that takes two arguments: the start and end indices of the current subtree we're working on. If the start index is greater than the end index, we've reached the end of a branch and we should return None.
    # Inside the build function, we pop the last value from the postorder list and create a new node with that value. Then, we use the inorder_map to find the index of the node in the inorder list.
    # Since we're working with the postorder traversal, we first recursively build the right subtree by calling build with the start index set to index + 1 and the end index set to end. Then, we recursively build the left subtree by calling build with the start index set to start and the end index set to index - 1.
    # Finally, we call the build function with the start index set to 0 and the end index set to len(inorder) - 1, which will build the entire tree. The build function will return the root node of the tree.
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {val:idx for idx,val in enumerate(inorder)}
        rootIdxPost = len(postorder)-1
        
        def build(left, right):
            nonlocal rootIdxPost
            if left > right:
                return None
            
            rootVal = postorder[rootIdxPost]
            root = TreeNode(rootVal)
            print(f"root {rootVal} has indexPost={rootIdxPost}, left={left}, right={right}")
            #Keep decrementing postIndex to get right subtree done first
            rootIdxPost -= 1
            rootIdxIn = inorderMap[root.val]
            root.right = build(rootIdxIn+1, right)
            root.left = build(left, rootIdxIn-1)
            return root
        return build(0, len(inorder)-1)
