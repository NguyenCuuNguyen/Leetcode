#Intersection of Two Linked Lists
#Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

#METHOD 1:  Calculate 2 LL's len, ignore the first extra nodes if any
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
            

#METHOD 2: split the both paths into s1 = s1_diff + common and s2 = s2_diff + common. 
#Two pointers will travel the same distance and will meet. First iteration accounts 
#for the difference in length and second iteration converge at intersection if any.

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        curA, curB = headA, headB
        while curA != curB: #not null
            curA = headB if curA is None else curA.next
            curB = headA if curB is None else curB.next
        return curA
            