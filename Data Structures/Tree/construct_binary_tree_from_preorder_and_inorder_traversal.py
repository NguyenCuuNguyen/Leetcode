#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#  Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#REVIEW THIS PROBLEM
class Solution:
     #SOLUTION 1:
     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map={val:idx for idx, val in enumerate(inorder)}
        preorder_idx=0

        def treeHelper(left, right):
            #Parent's call sets the limit to how far left and right indexes are:
            print(f"call treeHelper: left={left}, right={right}")
            nonlocal preorder_idx #take value from the nearest loop, initially from global scope.
            if left>right: 
                #because for left subtree: right=endIndex of leftsubtree, keeps decremented from root's index till -1
                #            right subtree: left keeps incremented till 
                print(f"===FAIL: left={left}, right = {right}")
                return None
            
            node_val = preorder[preorder_idx]
            print(f"NODE_VAL={node_val} and preorder index={preorder_idx}")
            root=TreeNode(node_val)
            preorder_idx+=1 #Increment preorder pointer which gets all leftsubtree nodes done first

            inorder_index=inorder_map[node_val]
            print(f"\t==call left branch: left={left}, inorder_index={inorder_index-1}") 
            root.left = treeHelper(left, inorder_index-1 ) #take left from parent's call, right is set to rootIndex-1
            print(f"\t==call right branch: inorder_index={inorder_index+1}, right={right}")
            root.right = treeHelper(inorder_index+1, right) #take right from parent's call, left is set to rootIndex+1
            print("\n")
            return root
        
        return treeHelper(0, len(inorder)-1)
     
    #SOLUTION 2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(root.val)
        left_size = len(inorder[:index])
        root.left = self.buildTree(preorder[1:left_size+1], inorder[:index])
        root.right = self.buildTree(preorder[1+left_size:], inorder[index+1:])
        return root
     
    #SOLUTION 2.1:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[1+index:], inorder[index+1:])
        return root

    #LESSON 1: Hashmap return index in constant time
    #LESSON 2: Can always REASSIGN/ complete node's values AFTER INITIATION. 
#numleft = number of elements in left subtree = length of list from 0 to root's index in inorder list. root is first elemetn of preorder list
#prestart = index of root 
# +---------------+--------------------------------+--------------------------------+----------------------+----------------------+
# |               | preStart                       | preEnd                         | inStart              | inEnd                |
# +---------------+--------------------------------+--------------------------------+----------------------+----------------------+
# | left subtree  | preStart +1                    | preStart + numleft +1          | inStart              | rootIndexInorder - 1 |
# |               |                                | = numberOfLeftTreeElements + 1 |                      |                      |
# +---------------+--------------------------------+--------------------------------+----------------------+----------------------+
# | right subtree | preStart + numleft +1          | preEnd                         | rootIndexInorder + 1 | InEnd                |
# |               | = numberOfLeftTreeElements + 1 |                                |                      |                      |
# +---------------+--------------------------------+--------------------------------+----------------------+----------------------+

        