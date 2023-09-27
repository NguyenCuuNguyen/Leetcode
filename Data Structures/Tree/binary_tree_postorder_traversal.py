#https://leetcode.com/problems/binary-tree-postorder-traversal/
class Solution:
    #SOLUTION 1: RECURSION
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        def postorder(root: Optional[TreeNode]):
            if not root:
                return None
            postorder(root.left)
            postorder(root.right)
            output.append(root.val)
        postorder(root)
        return output
        #Postorder traversal is defined as a type of tree traversal which follows the Left-Right-Root policy such that for each node:
            # The left subtree is traversed first
            # Then the right subtree is traversed
            # Finally, the root node of the subtree is traversed

    
    #Failed second attemp: ITERATIVE 
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return None
    output, stack = [],[]
    #Need to print left, right, root => push root, right, left 
    while True:
        while root != None:
            #push right child first, then root, then move left
            if root.right != None:
                stack.append(root.right)
            stack.append(root)
            root = root.left
        root = stack.pop()
        if len(stack) != 0:
            if root.right != None and root.right == stack[-1]:
                right_child = stack.pop()
                stack.append(root)
                root = root.right
        else:
            output.append(root.val)
            root = None
        if len(stack) <= 0:
            break
        return output