#Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#METHOD 1: ITERATTIVE
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return None
        while head != None and head.val == val:
            head = head.next 
        cur = head 
        while cur != None and cur.next != None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:  
                cur = cur.next
        return head
            
#METHOD 2: RECURSION - goes down to the last null node, and rebuilds the linked list
#by adding only the nodes which are not equal to val to this null, so it goes from
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return None
        head.next = self.removeElements(head.next, val)
        return head.next if head.val is val else head
            