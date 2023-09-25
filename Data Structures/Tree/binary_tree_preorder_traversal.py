#https://leetcode.com/problems/binary-tree-preorder-traversal/description/
class Solution:
    #SOLUTION 1: RECURSION:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def preorder(root: Optional[TreeNode]):
            if not root:
                return None
            output.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return output
    

    #SOLUTION 2 - MORRIS TRAVERSAL: ROOT, LEFT, RIGHT 
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        cur = root
        while cur != None:
            if cur.left == None:
                output.append(cur.val)
                cur = cur.right
            else:
                #Find predecessor:
                pred = cur.left
                while pred.right != None and pred.right != cur:
                    pred = pred.right
                if pred.right == None: #Create link to cur, visit left subtree
                    pred.right = cur
                    output.append(cur.val)
                    cur = cur.left
                else:  #link already exists, remove link & move right
                    pred.right = None
                    cur = cur.right
        return output
    
    #SOLUTION 3 - ITERATIVE:
    # Create an empty stack nodeStack and push root node to stack. 
    # Do the following while nodeStack is not empty. 
    # Pop an item from the stack and print it. 
    # Push right child of a popped item to stack 
    # Push left child of a popped item to stack
    # The right child is pushed before the left child to make sure that the left subtree is processed first.
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        output,stack = [],[]
        stack.append(root)
        print(f"stack is {stack}")
        while stack!= None:
            cur = stack.pop()
            if cur.right != None:
                stack.append(cur.right)
            if cur.left != None:
                stack.append(cur.left)
            output.append(cur.val)
        return output
    #LESSON 1: empty list is NOT NONE. To check for empty list, do either len(list)==0 or while list:

 #First attempt: Fail
        # output = []
        # cur = root
        # while cur != None:
        #     output.append(cur.val)
        #     if cur.left != None:
        #         cur = cur.left
        #     else:
        #         cur = cur.right
        # return output
    #LESSON 1: 