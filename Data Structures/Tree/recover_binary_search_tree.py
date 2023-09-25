#https://leetcode.com/problems/recover-binary-search-tree/description/

#SOLUTION 1: MORRIS INORDER TRAVERSAL
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre, first, second = None, None, None
        cur = root
        while cur != None:
            if not cur.left: #If reach end of left subtree root:
                if pre != None and pre.val > cur.val: #REVIEW: 
                    if first is None: #without this, wrong output [1,2,null,null,3]
                        first = pre
                        second = cur
                #First assignment of pre goes here
                pre = cur 
                cur = cur.right
            else: #find inorder predecessor aka rightmost node of left subtree:
                #Add a temp node to traverse & search for inorder predecssor aka rightmost node inleft substree:
                node = cur.left
                while node.right != None and node.right != cur:
                    node = node.right
                #After reaching inorder predecessor node, handle each scenario:
                #if predecessor.right is null, Create link
                if node.right == None:
                    node.right = cur
                    cur = cur.left
                #if predecessor.right is current, Restore tree
                else:
                    node.right = None
                    #Inorder predecessor or rightmost node of left subtree has to be smaller than current/root, check for that:
                    if pre != None and pre.val > cur.val:
                        if first is None: #WHY this cond? Without this, wrong output [2,3,null,null,1]. Without both, it fails for [1,3,null,null,2] because wrongly replace first=2 VS the correct first=3, second=1 in second visit to cur=1 to remove link.
                            first = pre
                            second = cur #WHY? because it's inside undesired condition of pre > cur
                    pre = cur #~visit
                    cur = cur.right
        if first != None and second != None: #REVIEW
            first.val, second.val = second.val, first.val

#LESSON 1: If prompt only requires to keep track of 2 nodes, then only store 2 nodes instead of the whole array of inorder nodes as traversing. Pay close attetion to prompt!