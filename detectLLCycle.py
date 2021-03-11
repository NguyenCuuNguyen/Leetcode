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