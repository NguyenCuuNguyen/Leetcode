#Intersection of Two Linked Lists
#Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curA, curB = headA, headB
        lenA, lenB = self.findLength(headA), self.findLength(headB)
        # bc we only care about intersection, extra length can be ignored
        while lenA > lenB:
            curA = curA.next
            lenA -= 1
        while lenB > lenA:
            curB = curB.next
            lenB -= 1

        while curA != None or curB != None:
            if curA == curB:
                return curA 
            curA = curA.next
            curB = curB.next
        else:
            return None
        
    def findLength(self, head):
        cur = head
        count = 1
        while cur:
            cur = cur.next
            count +=1
        return count
            