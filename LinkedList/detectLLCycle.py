#Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow = head, head
        #fast.next and fast.next.next --> NULL exception
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        else: 
            return None
                #find where slow and head meets
        while head != slow:
            head = head.next
            slow = slow.next
        return head

#Consider the following linked list, where E is the cylce entry and X, the crossing point of fast and slow.
#        H: distance from head to cycle entry E
#        D: distance from E to X
#        L: cycle length
#                          _____
#                         /     \
#        head_____H______E       \
#                        \       /
#                         X_____/   
        
    
#        If fast and slow both start at head, when fast catches slow, slow has traveled H+D and fast 2(H+D). 
#        Assume fast has traveled n loops in the cycle, we have:
#        2H + 2D = H + D + nL  -->  H + D = nL  --> H = nL - D
#        Thus if two pointers start from head and X, respectively, one first reaches E, the other also reaches E. 