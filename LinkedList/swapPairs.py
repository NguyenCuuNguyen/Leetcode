# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = ListNode(0)
        temp.next = head
        cur = temp
        while cur.next != None and cur.next.next != None:
            first = cur.next
            second = cur.next.next
            cur.next = second
            first.next = second.next
            cur.next.next = first
            cur = cur.next.next; 
            #points to the second node in newly swapped pair
        return temp.next
        