"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        p = head
        while p != None:
           #Case 1: no child, proceed
            if p.child is None:
                p = p.next
                continue # return control to while condition
            #Case 2: go to end of children node, 
            temp = p.child #to keep track of first and last node in child chain
            while temp.next != None:
                temp = temp.next
            #temp.next is None
            #connect child's ultimate end with p.next
            temp.next = p.next
            if p.next != None:  
                p.next.prev = temp
            #make p.child the p.next and make p.child null
            p.next = p.child 
            p.child.prev = p
            p.child = None
        return head

#EXAMPLE:  p                            
#  1---2---3---4---5---6--NULL          
#          |
#          7---8---9---10--NULL
#              |
#              11--12--NULL

#After detecting a child node, traverse to temp = 10:
#        p  p.child      temp p.nxt
#        |   |            |   |
#1---2---3---7---8---9---10---4---5---6--NULL          
#                |
#                11--12--NULL

#Bc 3's child is None, traverse to p = 8 and repeat
            
                
            