# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: ListNode)->ListNode:
        
        return head
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find the mid of list
        if not head: return []
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse second half
        prev, cur =  None, slow.next #slow = 3
        while cur: #cur is None when loop exits
            nxt = cur.next 
            cur.next = prev # takes care of nxt.next = cur
            prev = cur
            cur = nxt
        slow.next = None #need this line bc slow.next= 4, we want 4->None. prev.next is wrong bc prev = 5, 
        head2, head1 = prev, head #not prev.next bc 
        
        #splice the nodes of 2 lists in:
        while head2:
            nxt = head1.next #2
            head1.next = head2 # 1->5
            head1 = head2 #make 1 new head2
            head2 = nxt
           


class Solution:
    def reorderList(self, head):
        if head is None or head.next is None:
            return 
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        cur = head
        while cur != stack[-1] and cur.next != stack[-1]:
            lastNode = stack.pop()
            nxt = cur.next
            cur.next = lastNode
            cur.next.next = nxt
            cur = nxt
            stack[-1].next = None
        return 
