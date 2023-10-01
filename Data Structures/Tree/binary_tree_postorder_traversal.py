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

    #SOLUTION 2: Iterative
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        output, stack = [],[]
        cur = root
        #Use last visited node instead of peeking the stack

        cur = root
        lastVisited = 0
        #Need to print left, right, root => push root, right, left 
        while cur != None or len(stack) != 0:
            print(f"cur is {cur}\n stack={stack}")
            if cur != None:
                stack.append(cur)
                cur = cur.left
            else:
                temp = stack[-1] #This helps the popping in and out
                if temp.right != None and temp.right != lastVisited: #either way, visit cur next because left right root
                    cur = temp.right
                else:
                    stack.pop()
                    output.append(temp.val)
                    lastVisited = temp
        return output
    

    #Failed second attemp: ITERATIVE 
    #REVIEW THIS AND FIX 
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        output, stack = [],[]
        cur = root
        #Need to print left, right, root => push root, right, left 
        while True:
            while cur != None:
                #push right child first, then root, then move left
                if cur.right != None:
                    stack.append(cur.right)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if len(stack) != 0:
                if cur.right != None and cur.right == stack[-1]:
                    right_child = stack.pop()
                    stack.append(cur)
                    cur = right_child
            else:
                output.append(root.val)
                root = None
            if len(stack) <= 0:
                break
            return output